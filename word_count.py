# *** MY CODE ***
file_name = raw_input("Enter the name of a file: ")

num_of_characters = 0
num_of_words = 0
num_of_lines = 0
num_of_unique = 0
unique_words = []

user_file = open(file_name, "r")

for line in user_file:
    num_of_lines += 1
    
    words = line.split(" ")
    if words[0] != "\n":
        num_of_words += len(words)

    for char in line:
        num_of_characters += 1

    for word in words:
        if word not in unique_words and word != "\n":
            unique_words.append(word)

num_of_unique = len(unique_words)

print unique_words

print num_of_lines
print num_of_words
print num_of_characters
print num_of_unique

# *** HIS CODE ***
#filename = raw_input("Enter a filename: ")

#number_of_characters = 0
#number_of_words = 0
#unique_words = set()

#for number_of_lines, line in enumerate(open(filename), 1):
    #number_of_characters += len(line)
    #number_of_words += len(line.split())
    #unique_words.update(line.split())

#print("Number of lines: {}".format(number_of_lines))
#print("Number of characters: {}".format(number_of_characters))
#print("Number of words: {}".format(number_of_words))
#print("Number of unique words: {}".format(len(unique_words)))

