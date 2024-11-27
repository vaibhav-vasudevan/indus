tools = [
    {
        "type": "function",
        "function": {
            "name": "get_customer_info",
            "description": "Retrieves customer information based on a 7-digit customer code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "The 7-digit code identifying the customer.",
                    }
                },
                "required": ["customer_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "generate_quote",
            "description": "Generates a quote for a given product and customer, allowing for override pricing with manager approval.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "The 7-digit code identifying the customer.",
                    },
                    "product_id": {
                        "type": "string",
                        "description": "The product ID for which the quote is generated.",
                    },
                    "override_price": {
                        "type": "number",
                        "description": "The custom price for the product, requiring manager approval if specified.",
                    }
                },
                "required": ["customer_id", "product_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "process_order",
            "description": "Processes and logs a customer's order, including product details and pickup location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_data": {
                        "type": "object",
                        "description": "An object containing order details.",
                        "properties": {
                            "customer_id": {"type": "string", "description": "The customer ID for the order."},
                            "product_id": {"type": "string", "description": "The ID of the product ordered."},
                            "quantity": {"type": "integer", "description": "Quantity of the product ordered."},
                            "site_id": {"type": "string", "description": "ID of the pickup location."},
                        },
                        "required": ["customer_id", "product_id", "quantity", "site_id"]
                    }
                },
                "required": ["order_data"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_vendor_info",
            "description": "Retrieves vendor information for a specific product, including contact and shipping cost.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "The product ID for which vendor details are needed.",
                    }
                },
                "required": ["product_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_shipping_cost",
            "description": "Calculates the average shipping cost for a specified site.",
            "parameters": {
                "type": "object",
                "properties": {
                    "site_id": {
                        "type": "string",
                        "description": "The ID of the site where the shipment is to be delivered.",
                    }
                },
                "required": ["site_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "log_approval_request",
            "description": "Logs a request for manager approval for an overridden product price.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "The 7-digit customer ID for the approval request.",
                    },
                    "product_id": {
                        "type": "string",
                        "description": "The product ID for which approval is requested.",
                    },
                    "requested_price": {
                        "type": "number",
                        "description": "The custom price the sales rep wants to offer.",
                    }
                },
                "required": ["customer_id", "product_id", "requested_price"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "log_customer_interaction",
            "description": "Logs customer interactions, tracking details for future reference.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "The 7-digit ID of the customer involved in the interaction.",
                    },
                    "interaction_type": {
                        "type": "string",
                        "description": "The type of interaction, such as 'email' or 'phone'.",
                    },
                    "notes": {
                        "type": "string",
                        "description": "Notes about the interaction, like follow-up details or quotes discussed.",
                    }
                },
                "required": ["customer_id", "interaction_type", "notes"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_order_history",
            "description": "Fetches past order history for a specified customer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "The 7-digit customer ID for whom order history is needed.",
                    }
                },
                "required": ["customer_id"],
            },
        },
    }
]