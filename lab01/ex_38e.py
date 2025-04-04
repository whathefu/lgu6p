products = [
    {
        "category": "Electronics",
        "items": [
            {"name": "Laptop", "price": 1200, "stock": 5},
            {"name": "Smartphone", "price": 800, "stock": 10}
        ]
    },
    {
        "category": "Home Appliances",
        "items": [
            {"name": "Vacuum Cleaner", "price": 150, "stock": 7},
            {"name": "Air Conditioner", "price": 500, "stock": 3}
        ]
    }
]


# result = {
#     "Laptop": {"price": 1200, "stock": 5},
#     "Smartphone": {"price": 800, "stock": 10},
#     "Vacuum Cleaner": {"price": 150, "stock": 7},
#     "Air Conditioner": {"price": 500, "stock": 3}
# }


def convert_data(products):
    pass

R = {}
for i in products :
    a = i["items"]
    for j in a:
        # j: {"name": "Air Conditioner", "price": 500, "stock": 3}
        name = j['name']
        
        R[ j['name'] ] = {'price': j['price'], 'stock':j['stock']}

print(R)



    # # print(result)
    # result

