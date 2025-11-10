friends={"Rachel":"Ross","Monica":"Chandler","Phoebe":"Joey"}

name=input("Enter a key here: ")
if name in friends.keys():
    print("Name already exists.")

if name in friends.values():
    print("Value already")