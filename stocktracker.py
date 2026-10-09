inventory = {
    "apples": {"price": 1.20, "quantity": 25}, "bananas": {"price": 0.50, "quantity": 8}, "oranges": {"price": 0.80, "quantity": 12}, "milk": {"price": 3.50, "quantity": 4}, "bread": {"price": 2.20, "quantity": 18}
}
def check_low_stock(threshold):
    print("items with stock below threshold")
    for item_name, details in inventory.items():
        if details["quantity"] < threshold:
            print("item:", item_name, " quantity remaining:", details["quantity"], "price: $", details["price"])
check_low_stock(10)
print()
check_low_stock(5)
