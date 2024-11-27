product_catalog = {
    "Fasteners": [
        {"product_id": "F1001", "name": "Hex Bolt", "price": 0.75, "stock_level": 500},
        {"product_id": "F1002", "name": "Wood Screw", "price": 0.10, "stock_level": 1000},
        {"product_id": "F1003", "name": "Machine Screw", "price": 0.15, "stock_level": 750},
        {"product_id": "F1004", "name": "Nylon Nut", "price": 0.50, "stock_level": 600},
        {"product_id": "F1005", "name": "Wing Nut", "price": 0.20, "stock_level": 400},
    ],
    "Bearings": [
        {"product_id": "B1001", "name": "Ball Bearing", "price": 2.50, "stock_level": 150},
        {"product_id": "B1002", "name": "Roller Bearing", "price": 5.00, "stock_level": 100},
        {"product_id": "B1003", "name": "Thrust Bearing", "price": 7.00, "stock_level": 80},
        {"product_id": "B1004", "name": "Tapered Roller Bearing", "price": 4.50, "stock_level": 90},
        {"product_id": "B1005", "name": "Needle Bearing", "price": 3.75, "stock_level": 120},
    ],
    "Hydraulics": [
        {"product_id": "H1001", "name": "Hydraulic Hose", "price": 15.00, "stock_level": 200},
        {"product_id": "H1002", "name": "Hydraulic Cylinder", "price": 120.00, "stock_level": 30},
        {"product_id": "H1003", "name": "Pressure Gauge", "price": 20.00, "stock_level": 150},
        {"product_id": "H1004", "name": "Control Valve", "price": 75.00, "stock_level": 60},
        {"product_id": "H1005", "name": "Hydraulic Pump", "price": 200.00, "stock_level": 25},
    ],
    "Electrical Components": [
        {"product_id": "E1001", "name": "Solenoid Valve", "price": 30.00, "stock_level": 100},
        {"product_id": "E1002", "name": "Limit Switch", "price": 10.00, "stock_level": 300},
        {"product_id": "E1003", "name": "Circuit Breaker", "price": 25.00, "stock_level": 75},
        {"product_id": "E1004", "name": "Contactor", "price": 40.00, "stock_level": 80},
        {"product_id": "E1005", "name": "Relay", "price": 8.00, "stock_level": 200},
    ],
    "Pneumatics": [
        {"product_id": "P1001", "name": "Air Hose", "price": 10.00, "stock_level": 250},
        {"product_id": "P1002", "name": "Air Filter", "price": 15.00, "stock_level": 140},
        {"product_id": "P1003", "name": "Pressure Regulator", "price": 35.00, "stock_level": 100},
        {"product_id": "P1004", "name": "Quick Coupler", "price": 5.00, "stock_level": 300},
        {"product_id": "P1005", "name": "Pneumatic Cylinder", "price": 60.00, "stock_level": 50},
    ]
}

customer_database = [
    {"customer_id": "1000001", "name": "Alpha Industries", "contact": "John Doe", "email": "john.doe@alphaindustries.com", "phone": "555-1234"},
    {"customer_id": "1000002", "name": "Beta Solutions", "contact": "Jane Smith", "email": "jane.smith@betasolutions.com", "phone": "555-5678"},
    {"customer_id": "1000003", "name": "Gamma Corp", "contact": "Bill Turner", "email": "bill.turner@gammacorp.com", "phone": "555-9101"},
    {"customer_id": "1000004", "name": "Delta Manufacturing", "contact": "Sue Kim", "email": "sue.kim@deltamfg.com", "phone": "555-1122"},
    {"customer_id": "1000005", "name": "Epsilon Enterprises", "contact": "Bob Brown", "email": "bob.brown@epsilonenterprises.com", "phone": "555-3344"},
    {"customer_id": "1000006", "name": "Zeta Tech", "contact": "Alice Johnson", "email": "alice.johnson@zetatech.com", "phone": "555-5566"},
    {"customer_id": "1000007", "name": "Eta Services", "contact": "Carlos Martinez", "email": "carlos.martinez@etaservices.com", "phone": "555-7788"},
    {"customer_id": "1000008", "name": "Theta Solutions", "contact": "Nancy Wilson", "email": "nancy.wilson@thetasolutions.com", "phone": "555-9900"},
    {"customer_id": "1000009", "name": "Iota Innovations", "contact": "Peter Wong", "email": "peter.wong@iotainnovations.com", "phone": "555-2233"},
    {"customer_id": "1000010", "name": "Kappa Manufacturing", "contact": "Linda Garcia", "email": "linda.garcia@kappamfg.com", "phone": "555-4455"},
    {"customer_id": "1000011", "name": "Lambda Logistics", "contact": "George Hall", "email": "george.hall@lambdalogistics.com", "phone": "555-6677"},
    {"customer_id": "1000012", "name": "Mu Solutions", "contact": "Rebecca Adams", "email": "rebecca.adams@musolutions.com", "phone": "555-8899"},
    {"customer_id": "1000013", "name": "Nu Enterprises", "contact": "James Carter", "email": "james.carter@nuenterprises.com", "phone": "555-1010"},
    {"customer_id": "1000014", "name": "Xi Innovations", "contact": "Megan Lee", "email": "megan.lee@xiinnovations.com", "phone": "555-2323"},
    {"customer_id": "1000015", "name": "Omicron Tech", "contact": "Andrew Baker", "email": "andrew.baker@omicrontech.com", "phone": "555-4545"},
    {"customer_id": "1000016", "name": "Pi Components", "contact": "Emily Clark", "email": "emily.clark@picomponents.com", "phone": "555-6767"},
    {"customer_id": "1000017", "name": "Rho Systems", "contact": "Henry Young", "email": "henry.young@rhosystems.com", "phone": "555-8989"},
    {"customer_id": "1000018", "name": "Sigma Resources", "contact": "Diana King", "email": "diana.king@sigmaresources.com", "phone": "555-9090"},
    {"customer_id": "1000019", "name": "Tau Equipment", "contact": "Chris Walker", "email": "chris.walker@tauequipment.com", "phone": "555-3131"},
    {"customer_id": "1000020", "name": "Upsilon Tech", "contact": "Laura Scott", "email": "laura.scott@upsilontech.com", "phone": "555-5353"},
    {"customer_id": "1000021", "name": "Phi Solutions", "contact": "Oscar Ramirez", "email": "oscar.ramirez@phisolutions.com", "phone": "555-7575"},
    {"customer_id": "1000022", "name": "Chi Ventures", "contact": "Grace Kim", "email": "grace.kim@chiventures.com", "phone": "555-9797"},
    {"customer_id": "1000023", "name": "Psi Industries", "contact": "Victor Diaz", "email": "victor.diaz@psiindustries.com", "phone": "555-1919"},
    {"customer_id": "1000024", "name": "Omega Manufacturing", "contact": "Sophia Harris", "email": "sophia.harris@omegamfg.com", "phone": "555-3434"},
    {"customer_id": "1000025", "name": "Apex Solutions", "contact": "Zachary Wilson", "email": "zachary.wilson@apexsolutions.com", "phone": "555-5656"},
]

# Mock Communication History Database
communication_history = [
    {"customer_id": "1000001", "product_id": "F1001", "date": "2023-10-15", "interaction_type": "email", "notes": "Negotiated 5% discount"},
    {"customer_id": "1000002", "product_id": "E1001", "date": "2023-09-30", "interaction_type": "phone", "notes": "Confirmed regular order"},
    {"customer_id": "1000003", "product_id": "H1003", "date": "2023-10-01", "interaction_type": "email", "notes": "Customer requested shipping update"},
    {"customer_id": "1000004", "product_id": "B1002", "date": "2023-09-15", "interaction_type": "email", "notes": "Adjusted price after negotiation"},
    {"customer_id": "1000005", "product_id": "P1005", "date": "2023-10-10", "interaction_type": "email", "notes": "Repeat order, no quote requested"},
]

# Mock Order History Database
order_history = [
    {"order_id": "O1001", "customer_id": "1000001", "product_id": "F1001", "quantity": 100, "order_date": "2023-09-01"},
    {"order_id": "O1002", "customer_id": "1000002", "product_id": "E1002", "quantity": 5, "order_date": "2023-08-15"},
    {"order_id": "O1003", "customer_id": "1000003", "product_id": "H1002", "quantity": 2, "order_date": "2023-09-20"},
    {"order_id": "O1004", "customer_id": "1000004", "product_id": "B1004", "quantity": 50, "order_date": "2023-09-30"},
    {"order_id": "O1005", "customer_id": "1000005", "product_id": "P1001", "quantity": 150, "order_date": "2023-08-25"},
]

# Mock Vendor Database
vendor_database = [
    {"vendor_id": "V1001", "name": "Fastener Co.", "product_id": "F1001", "contact": "Mike Rowe", "email": "mike@fastenerco.com", "phone": "555-1111", "shipping_cost": 15.00},
    {"vendor_id": "V1002", "name": "Bearing Supplies", "product_id": "B1001", "contact": "Lisa Tran", "email": "lisa@bearingsupplies.com", "phone": "555-2222", "shipping_cost": 20.00},
    {"vendor_id": "V1003", "name": "Hydraulic Solutions", "product_id": "H1003", "contact": "Tom Harris", "email": "tom@hydraulicsolutions.com", "phone": "555-3333", "shipping_cost": 30.00},
    {"vendor_id": "V1004", "name": "Pneumatic Pros", "product_id": "P1001", "contact": "Sam Patel", "email": "sam@pneumaticpros.com", "phone": "555-4444", "shipping_cost": 25.00},
    {"vendor_id": "V1005", "name": "Electrical Depot", "product_id": "E1003", "contact": "Jill Murray", "email": "jill@electricaldepot.com", "phone": "555-5555", "shipping_cost": 18.00},
]

# Mock Approval Log
approval_log = [
    {"approval_id": "A1001", "customer_id": "1000001", "product_id": "F1001", "requested_price": 0.70, "approved_price": 0.72, "manager_approval": True, "approval_date": "2023-10-01"},
    {"approval_id": "A1002", "customer_id": "1000002", "product_id": "E1001", "requested_price": 480, "approved_price": 485, "manager_approval": True, "approval_date": "2023-09-20"},
    {"approval_id": "A1003", "customer_id": "1000003", "product_id": "H1001", "requested_price": 14.00, "approved_price": None, "manager_approval": False, "approval_date": "2023-09-28"},
    {"approval_id": "A1004", "customer_id": "1000004", "product_id": "B1004", "requested_price": 4.25, "approved_price": 4.30, "manager_approval": True, "approval_date": "2023-09-18"},
    {"approval_id": "A1005", "customer_id": "1000005", "product_id": "P1005", "requested_price": 55.00, "approved_price": None, "manager_approval": False, "approval_date": "2023-10-12"},
]

# Mock Shipping Information Database
shipping_info = [
    {"site_id": "S1001", "location": "Warehouse 1", "address": "123 Industrial Way, Anytown, USA", "average_shipping_cost": 25.00},
    {"site_id": "S1002", "location": "Warehouse 2", "address": "456 Manufacturing St, Anytown, USA", "average_shipping_cost": 30.00},
    {"site_id": "S1003", "location": "Distribution Center", "address": "789 Supply Ave, Anytown, USA", "average_shipping_cost": 20.00},
    {"site_id": "S1004", "location": "Main Office", "address": "101 Corporate Blvd, Anytown, USA", "average_shipping_cost": 15.00},
    {"site_id": "S1005", "location": "Satellite Site", "address": "202 Industrial Blvd, Anytown, USA", "average_shipping_cost": 28.00},
]