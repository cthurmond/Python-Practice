people = [('Barack', 'Obama', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

# *** MY CODE ***
for person in people:
    print ("{0:10s} {1:10s} {2:5.2f}").format(person[1], person[0], person[2])

# *** HIS CODE ***
#for person in sorted(people, key=lambda person: (person[1], person[0])):
       # print("{1:10} {0:10} {2:5.2f}".format(*person))