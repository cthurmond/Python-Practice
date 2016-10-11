mylist = list(range(100))

# *** My Answer ***

#mylist = ["a" for x, y in enumerate(mylist) if y < 6]
#if len(mylist) < 6:
  #  for i in range(6 - len(mylist)):
    #    mylist.append("a")

mylist[:] = ["a"] * 6

print (mylist)