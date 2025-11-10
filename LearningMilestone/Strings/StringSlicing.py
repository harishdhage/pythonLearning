str = "Apple Mango Banana"
print(len(str))
#Start from 1st index 0 and last index mentioned is
print(str[2:7])
#Counts only first 7 char start from index 0
print(str[:7])
#Skips first 5 char start from 0 index
print(str[5:])
#str[-5,-2] : Here -5 start counting char from last starts at index 1, -2 is after reaching 5 char then count 2 char start from index 0
print(str[-5:-2])
#String reverse
print(str[-1:])
#without using indexes
print(str[:])


#The left operand must be smaller than the operand on right, for getting a substring of the original string. Python doesn't raise any error, if the left operand is greater, bu returns a null string.
print ("str[-1:7]:", str[-1:7])
print ("str[7:0]:", str[7:0])

#Substring from returned sub-string
print(str[:6][:3])
print(str[:6][:10])

#String reverse
print(str[::-1])

#Alternative element from String
print(str[::2])
