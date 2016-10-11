user_input = raw_input("Enter a word to be translated to Pig Latin: ")

if user_input[0].lower() in ("aeiou"):
    print (user_input + "way")
else:
    print (user_input[1:] + user_input[0] + "ay")