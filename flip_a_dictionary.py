mydict = {1: "ONE", 2: "TWO", 3: "THREE"}

# *** MY CODE ***
for key, elem in mydict.items():
    del mydict[key]
    mydict[elem] = key

print mydict

# *** HIS CODE ***
#{value:key for key, value in d.items() }

# *** HIS OTHER CODE ***
#output = { }
#for key in d:
    #output[d[key]] = key