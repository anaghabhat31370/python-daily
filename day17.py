questions = [
    ("What is 2 + 2?", "4"),
    ("What is the capital of Japan?", "tokyo"),
    ("How many planets are in the Solar System?", "8")
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
