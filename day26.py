cart = []

while True:
    item = input("Enter an item (or type 'done'): ")

    if item.lower() == "done":
        break

    cart.append(item)

print("\nYour shopping cart:")

for item in cart:
    print("-", item)

print("Total items:", len(cart))
