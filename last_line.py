# *** MY CODE ***

text_file = raw_input("Enter the name of a text file: \n")

user_file = open(text_file, 'r')

lines = user_file.readlines()

print lines[len(lines) - 1:]

# *** HIS CODE ***

#file_name = raw_input("Enter a filename: ")
#print (open(filename).readlines()[-1])