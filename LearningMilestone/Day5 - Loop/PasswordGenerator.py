import random

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

password_length = int(input("Enter required password length :"))
alpha_range = int(input("Enter the number of the alphabet charecter in the password : "))
num_range = int(input("Enter the numeric character count to be added in password : "))
spChar_range = int(input("Enter the number of the special charecter in password : "))
enteredPswdLength = alpha_range+num_range+spChar_range
password_list=""
if enteredPswdLength == password_length:
    for char in range(0, alpha_range):
        password_list += random.choice(alphabets)
    for char in range(0, spChar_range):
        password_list += random.choice(special_char)
    for char in range(1, num_range+1):
        password_list += random.choice(numbers)
    print(f"Password is : {password_list}")
else:
    print("Required password length and enteredPswdLength not equal!!!")

# Other Solution
pwsd_list=[]
if enteredPswdLength == password_length:
    for char in range(0, alpha_range):
        pwsd_list.append(random.choice(alphabets))
    for char in range(0, spChar_range):
        pwsd_list.append(random.choice(special_char))
    for char in range(1, num_range+1):
        pwsd_list.append(random.choice(numbers))
    print(f"password : {pwsd_list}")
    random.shuffle(pwsd_list)
    print(pwsd_list)
else:
    print("Required password length and enteredPswdLength not equal!!!")

password=""
for char in pwsd_list:
    password += char

print(f"Password is : {password}")