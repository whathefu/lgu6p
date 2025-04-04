orders = [
    {
        "country": "USA",
        "customers": [
            {
                "customer_id": "C001",
                "orders": [
                    {"product": "Laptop", "quantity": 1, "unit_price": 1200},
                    {"product": "Mouse", "quantity": 2, "unit_price": 25}
                ]
            },
            {
                "customer_id": "C002",
                "orders": [
                    {"product": "Smartphone", "quantity": 1, "unit_price": 800}
                ]
            }
        ]
    },
    {
        "country": "Canada",
        "customers": [
            {
                "customer_id": "C003",
                "orders": [
                    {"product": "Laptop", "quantity": 2, "unit_price": 1150},
                    {"product": "Keyboard", "quantity": 1, "unit_price": 100}
                ]
            }
        ]
    }
]

result = {}
for i in orders :
    a = i["customers"]

    for j in a:
        #  j는 고객의 사전 
        id = j['customer_id']
        ord = j['orders']
        
        prods = []
        total = 0

        for p in ord :
            # p는 개별주문
            prods.append(p['product'])

            total += p['unit_price']*p['quantity']

            result[j['customer_id']]={'country':i["country"],
                                      'prodcuct':prods, 
                                      'total_amount':total}

print(result)





# result = {
#     "C001": {
#         "country": "USA",
#         "products": ["Laptop", "Mouse"],
#         "total_amount": 1250  # (1 x 1200) + (2 x 25)
#     },
#     "C002": {
#         "country": "USA",
#         "products": ["Smartphone"],
#         "total_amount": 800
#     },
#     "C003": {
#         "country": "Canada",
#         "products": ["Laptop", "Keyboard"],
#         "total_amount": 2400  # (2 x 1150) + (1 x 100)
#     }
# }






# def order_by_customers(orders):
#     pass

