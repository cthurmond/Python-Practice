def strsort(string):
    listToSort = []
    for letter in string:
        listToSort.append(letter)
    listToSort.sort()
    sortString = "".join(listToSort)
    return sortString

sortedString = strsort("zyxwvutsrqponmlkjihgfedcba")
print (sortedString)


