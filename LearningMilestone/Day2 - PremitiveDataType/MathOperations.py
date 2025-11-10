print(12+32)
print(32-21)
print(12*32)
print(5/3)
print(5//3)
print(2**3) #Exponent

#PEMDAS - Paranthesis, Exponent, Muliplication/Division, Addission/Subtraction
print(3 * (3 + 3) / 3 - 3 ** 3)

height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight/height**2
print(bmi)
print(round(bmi))
print(round(bmi, 2))

#Increment, decrement operator
score = 0
score += 1
score -= 1
score =- 2 # assign value
score += 1
score *= 3
score /= 5
print("Your scrore is "+ str(score))

#f String
print(f"Your score is - {score}")