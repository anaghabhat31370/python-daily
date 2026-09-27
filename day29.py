cart = []

while True:
    print("\n1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item: ")
        cart.append(item)
        print("Item added!")

    elif choice == "2":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("Your cart:")
            for i, item in enumerate(cart, 1):
                print(i, item)

    elif choice == "3":
        item = input("Enter item to remove: ")

        if item in cart:
            cart.remove(item)
            print("Item removed!")
        else:
            print("Item not found.")

    elif choice == "4":
        print("Shopping complete!")
        break

    else:
        print("Invalid choice.")
