score = 0

answer = input("What is the capital of India? ")

if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("How many sides does a triangle have? ")

if answer == "3":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What planet do we live on? ")

if answer.lower() == "earth":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What is 5 + 5? ")

if answer == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your score is", score, "out of 5")
