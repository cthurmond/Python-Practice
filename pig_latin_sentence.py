userInput = raw_input("Enter a sentence to be translated into \
Pig Latin:\n")

wordList = userInput.split()
newList = []

for word in wordList:
    if word[0].lower() in ("aeiou"):
        newList.append(word + "way")
    else:
        newList.append(word[1:] + word[0] + "ay")

translatedSentence = " ".join(newList)
print translatedSentence