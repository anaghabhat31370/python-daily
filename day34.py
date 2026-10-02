text = input("Enter a sentence: ")
vowels = "aeiou"
vowel_count = 0
character_count = {}
for char in text.lower():
    if char in vowels:
        vowel_count += 1
    if char.isalpha():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
words = text.split()
print("Number of words:", len(words))
print("Number of vowels:", vowel_count)
print("Character frequencies:", character_count)
if character_count:
    most_common = max(character_count, key=character_count.get)
    print("Most common character:", most_common)
    print("Frequency:", character_count[most_common])
