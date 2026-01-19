s1 = 'Apple' 
print(id(s1))
s1 = 'Mango' # This is reassignment, creates new string object
print(id(s1))
s1[2]='X' # This will raise error as strings are immutable, we cannot change value at specific index
print(id(s1))