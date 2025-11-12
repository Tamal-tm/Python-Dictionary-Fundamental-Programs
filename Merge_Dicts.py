# Using Bar operator

dict1={"John":89,"Lisa":45}
dict2={"Lisa":94,"Peter":77}

print(dict1 | dict2) 

# Using ** Operator.

dict1={"John":89,"Lisa":45}
dict2={"Lisa":94,"Peter":77}

print({**dict1,**dict2})

# Using Copy and Update method

dict1={"John":89,"Lisa":45}
dict2={"Lisa":94,"Peter":77}

dict3=dict2.copy()
dict3.update(dict1)


print(dict3)












