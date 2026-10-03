
students = {
    "Aarav": 85,
    "Diya": 92,
    "Kabir": 67,
    "Meera": 38,
    "Rohan": 74
}

total = 0
passed = 0

for name, marks in students.items():
    total += marks

    if marks >= 40:
        passed += 1

average = total / len(students)
topper = max(students, key=students.get)

print("Class average:", average)
print("Topper:", topper)
print("Students passed:", passed)
print("Students failed:", len(students) - passed)
