# *** MY CODE ***
# Fixed brackets after looking at his code.
def dictdiff(d1, d2):
    diffdict = {}
    error_dict = ""
    for key in d1:
        try:
            if d1[key] != d2[key]:
                diffdict[key] = [d1[key], d2[key]]
        except KeyError:
            diffdict[key] = [d1[key], "none"] 
    for key in d2:
       if key not in d1:
            diffdict[key] = ["none", d2[key]]

    return diffdict

# *** HIS CODE ***
#def dictdiff(d1, d2):
    #output = {}
    #all_keys = sert(d1.keys())
    #all_keys.update(d2.keys())

    #for key in all_keys:
        #if d1.get(key) != d2.get(key):
            #output[key] = [d1.get(key), d2.get(key)]
    #return output


d1 = {"a":1, "b":2, "c":3}
d2 = {"a":1, "b":2, "c":4}

print ("First Test")
print (dictdiff(d1, d1))
print ("\n")

print ("Second Test")
print (dictdiff(d1, d2))
print ("\n")

d1 = {"a":1, "b":2, "d":3}
d2 = {"a":1, "b":2, "c":4}

print ("Third Test")
print (dictdiff(d1, d2))
print ("\n")

d1 = {"a":1, "b":2, "c":3}
d2 = {"a":1, "b":2, "d":4}

print ("Fourth Test")
print (dictdiff(d1, d2))