# Using 3rd variablr


from pathlib import Path

Path("C:/Users/catas/Downloads/Dajal Materials/Essentials/new-dict/demo-dict").mkdir(parents=True, exist_ok=True) # Takes two parameters(uses logic)(needed in some scenarios) Will create a new directory



# If we run again, will give error, since same file exists. So to not have any erroe, exists_ok=True. Default value is False.
