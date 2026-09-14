expenses = {}

for i in range(3):
    item = input("What did you spend on? ")
    amount = int(input("How much? ₹"))
    expenses[item] = amount

print("\nYour expenses:")

for item, amount in expenses.items():
    print(item, "→ ₹", amount)

print("Total spent: ₹", sum(expenses.values()))
