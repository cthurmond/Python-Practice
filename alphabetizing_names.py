people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
{'first':'Barack', 'last':'Obama', 'email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
]
# *** MY CODE ***
#for person in people:
    #print (person['last'] + ", " + person['first'] + ": " + person['email'])

# *** HIS CODE ***
for person in sorted(people, key=lambda person: [person['last'], person['first']]):
    print("{last}, {first}: {email}".format(**person))
