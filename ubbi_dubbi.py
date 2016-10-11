userInput = raw_input("Enter a word to translate into Ubbi Dubbi:\n")
translatedWord = ""

for char in userInput:
    if char in ("aeiou"):
        translatedWord += "ub" + char
    else:
        translatedWord += char

print translatedWord
