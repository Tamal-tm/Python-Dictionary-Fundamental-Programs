marks={"John":42,'Natalie':89,"Kinland":50} # Key stands at 0, value stands at 1
print(marks)

# Based on values

sv=sorted(marks.items(), key= lambda x : x[1])
print(sv) # List in dictionary format

# Sort only with values.

v=sorted(marks.values())
print(v)

v=sorted(marks.keys())
print(v)