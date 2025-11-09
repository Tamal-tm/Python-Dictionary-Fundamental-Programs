friends={"Rachel":"Ross","Monica":"Chandler","Phoebe":'Joe'}
print(friends)

print(friends["Monica"])

# Using items

for key, value in friends.items():
    print(key,"-", value)

# Using keys

for key in friends:
    print(key, ":", friends[key])

# Using keys and values

for key in friends.keys():
    print(key)

for i in friends.values():

    print(i)

