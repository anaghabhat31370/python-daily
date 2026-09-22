contacts = {}

while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact saved!")

    elif choice == "2":
        if contacts:
            for name, number in contacts.items():
                print(name, ":", number)
        else:
            print("No contacts saved.")

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
