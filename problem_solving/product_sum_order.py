from collections import defaultdict
orders =[
    {"Product": "apple", "quantity": 5},
    {"Product": "banana", "quantity": 2},
    {"Product": "apple", "quantity": 3}
]

grouped = defaultdict(int)
for order in orders:
    grouped[order["Product"]] += order["quantity"]

grouped_orders = dict(grouped)

print(grouped_orders)

