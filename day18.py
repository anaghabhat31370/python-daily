balance = 5000

def show_balance():
    print("Current balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print("Deposit successful!")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdrawal successful!")

while True:
    print("\n--- ATM ---")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
