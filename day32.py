text = input("Enter a word or sentence: ")

frequency = {}

for char in text.lower():
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("Character frequency:")

for char, count in frequency.items():
    print(char, ":", count)
