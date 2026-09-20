items = []

while True:
    item = input("Enter item name (or type 'done'): ")

    if item.lower() == "done":
        break

    price = float(input("Enter price: "))
    items.append((item, price))

total = 0

print("\n--- BILL ---")

for item, price in items:
    print(item, "₹", price)
    total += price

print("Total: ₹", total)
