# *** MY CODE ***

import os

longest_word = {}
directory = raw_input("Enter a directory: ")

for user_file in os.listdir(directory):
    if os.path.isfile(user_file):
        long_word = ""
        with open(user_file, "r") as f:
            for line in f:
                for word in line.split():
                    if len(word) > len(long_word):
                        long_word = word
        longest_word[user_file] = long_word

for key in longest_word:
    print (key + ": " + longest_word[key])

# *** HIS CODE ***

#import os
#dirname = raw_input("Enter a directory name: ")

#def longest_word(filename):
    #return sorted(open(filename).read().split(), key=len, reverse=True)[0]

#print ({filename : os.path.join(dirname, filename) for filename
    #in os.listdir(dirname)
    #if os.path.isfile(os.path.join(dirname, filename)) })