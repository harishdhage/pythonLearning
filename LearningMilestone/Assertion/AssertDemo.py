
numb = int(input("Enter a number between 1 to 100 : "))
assert numb>0 and numb<=100
print("Valid number")


code = input("Enter a 4 digit  : ")
print("Validating the code length", len(code))
assert len(code) == 4, "Valid code length"
assert len(code)!=4, "In-Valid code length"