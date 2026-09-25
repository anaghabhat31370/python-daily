questions = [
    ("What is 5 + 7?", "12"),
    ("What is the capital of France?", "paris"),
    ("How many days are in a week?", "7")
]

score = 0

for question, answer in questions:
    user_answer = input(question + " ")

    if user_answer.lower() == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Final score:", score, "/", len(questions))
