str = "Jackfruit"
str = "Mango"
print(str)
print(len(str))
print(str + "\tJuice")
print(len(str))
str2 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(str2)

#Check the part of string
print("tempor" in str2)
print("tempor" not in str2)

if "magna" in str2:
    print("String - magna present in phrase")
else:
    print("No present")

#Loop through the string by char
for char in str:
    print(char)