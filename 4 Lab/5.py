n = int(input("Введите количество записей о покупках: "))
purchase_dict = {}

for i in range(n):
    record = input().split()
    customer_id = int(record[0])
    product = record[1]
    quantity = int(record[2])
if customer_id in purchase_dict:
    if product in purchase_dict[customer_id]:
        purchase_dict[customer_id][product] += quantity
    else:
        purchase_dict[customer_id][product] = quantity
else:
    purchase_dict[customer_id] = {product: quantity}
for customer_id, purchases in purchase_dict.items():
    print("Покупатель с ID", customer_id, "купил:")
for product, quantity in purchases.items():
    print(product, "-", quantity)