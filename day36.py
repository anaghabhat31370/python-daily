
code = {
    "@": "a",
    "#": "e",
    "$": "i",
    "%": "o",
    "&": "u",
    "7": "s",
    "8": "t",
    "9": "n"
}

message = "@ 7#@8"

decoded = ""

for character in message:
    if character in code:
        decoded += code[character]
    else:
        decoded += character

print("Decoded message:", decoded)
