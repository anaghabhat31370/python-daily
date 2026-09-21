total = float(input("Enter total bill: "))
people = int(input("How many people? "))

if people > 0:
    each_person = total / people
    print("Each person pays:", round(each_person, 2))
else:
    print("Number of people must be greater than 0")
