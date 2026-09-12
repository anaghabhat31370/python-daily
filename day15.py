def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Invalid operation"

print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))
print(calculate(20, 4, "/"))
