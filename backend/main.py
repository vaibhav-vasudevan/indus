from fastapi import FastAPI

app = FastAPI()

from mock import *
from tooldef import tools
import json
import cohere

co = cohere.ClientV2(api_key="")

# Mock Databases
customers = customer_database
products = product_catalog
communication_history_log = communication_history
order_history_log = order_history
vendor_database_log = vendor_database
approval_log_entries = approval_log
shipping_info_log = shipping_info

# Function Definitions

# 1. Customer Lookup Function
def get_customer_info(customer_id):
    for customer in customers:
        if customer["customer_id"] == customer_id:
            return customer
    return {"error": "Customer not found"}

# 2. Quote Generation and Override
def generate_quote(customer_id, product_id, override_price=None):
    # Retrieve customer and product details
    customer = get_customer_info(customer_id)
    if "error" in customer:
        return customer

    # Mock quote from SAP (this would normally be fetched from SAP directly)
    for category, items in products.items():
        for item in items:
            if item["product_id"] == product_id:
                quote = item["price"]

                # Apply override price if provided
                if override_price is not None:
                    approval_required = True  # Assume manager approval is needed
                    approval_request = log_approval_request(customer_id, product_id, override_price)
                    return {
                        "customer": customer,
                        "product": item,
                        "quoted_price": override_price,
                        "approval": approval_request
                    }
                
                return {
                    "customer": customer,
                    "product": item,
                    "quoted_price": quote
                }
    return {"error": "Product not found"}

# 3. Order Processing
def process_order(order_data):
    order_id = f"O{len(order_history_log) + 1:04d}"  # Generate unique order ID
    order_data["order_id"] = order_id
    order_history_log.append(order_data)
    return {"status": "Order processed", "order_id": order_id}

# 4. Vendor and Shipping Cost Lookup
def get_vendor_info(product_id):
    for vendor in vendor_database_log:
        if vendor["product_id"] == product_id:
            return vendor
    return {"error": "Vendor not found"}

def calculate_shipping_cost(site_id):
    for site in shipping_info_log:
        if site["site_id"] == site_id:
            return site["average_shipping_cost"]
    return {"error": "Shipping site not found"}

# 5. Approval Log Function
def log_approval_request(customer_id, product_id, requested_price):
    approval_id = f"A{len(approval_log_entries) + 1:04d}"  # Generate unique approval ID
    approval_entry = {
        "approval_id": approval_id,
        "customer_id": customer_id,
        "product_id": product_id,
        "requested_price": requested_price,
        "approved_price": None,
        "manager_approval": False,
        "approval_date": None
    }
    approval_log_entries.append(approval_entry)
    return {"status": "Approval request logged", "approval_id": approval_id}

# 6. Customer Communication Log
def log_customer_interaction(customer_id, interaction_type, notes):
    interaction = {
        "customer_id": customer_id,
        "interaction_type": interaction_type,
        "notes": notes,
        "date": "2024-11-09"  # Current date (mocked here)
    }
    communication_history_log.append(interaction)
    return {"status": "Interaction logged"}

# 7. Repeat Order and Order History Retrieval
def get_order_history(customer_id):
    orders = [order for order in order_history_log if order["customer_id"] == customer_id]
    return orders if orders else {"error": "No orders found for this customer"}

functions_map = {
    "get_customer_info": get_customer_info,
    "generate_quote": generate_quote,
    "process_order": process_order,
    "get_vendor_info": get_vendor_info,
    "calculate_shipping_cost": calculate_shipping_cost,
    "log_approval_request": log_approval_request,
    "log_customer_interaction": log_customer_interaction,
    "get_order_history": get_order_history
}

system_message = """
## Task & Context
You help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user's needs as best you can, which will be wide-ranging.

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.
"""

@app.get("/{message}")
async def root(message: str):
    # Create messages array with system message and user message
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": message},
    ]

    # Get initial response with tool calls
    response = co.chat(
        model="command-r-plus-08-2024",
        messages=messages,
        tools=tools
    )

    # Process tool calls
    for tc in response.message.tool_calls:
        tool_result = functions_map[tc.function.name](**json.loads(tc.function.arguments))
        tool_content = []
        for data in tool_result:
            tool_content.append({"type": "document", "document": {"data": json.dumps(data)}})
        messages.append(
            {"role": "tool", "tool_call_id": tc.id, "content": tool_content}
        )

    # Get final response
    final_response = co.chat(
        model="command-r-plus-08-2024",
        messages=messages,
        tools=tools
    )

    # Return tool plan and final answer
    return {
        "tool_plan": response.message.tool_plan,
        "final_answer": final_response.message.content[0].text
    }
