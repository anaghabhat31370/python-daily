expenses = []

while True:
    item = input("Enter expense name (or type 'done'): ")

    if item.lower() == "done":
        break

    amount = float(input("Enter amount: "))

    expenses.append((item, amount))

print("\nYour Expenses:")

total = 0

for item, amount in expenses:
    print(item, ":", amount)
    total += amount

print("Total spent:", total)
