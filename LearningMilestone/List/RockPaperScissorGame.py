import random

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

image = [rock,paper,scissors]
user_input = int(input("Enter 1 for rock or 2 for paper or 3 for scissor"))
print(image[user_input])

if user_input >= 0 and user_input <= 2:
    comp_input = random.randint(0, 2)
    print(f"Computer entry : {comp_input}")
    print(image[comp_input])
    if user_input == 0 and comp_input == 2:
        print("You won")
    elif user_input < comp_input:
        print("You lost")
    elif user_input > comp_input:
        print("You won")
    elif user_input == comp_input:
        print("Its draw")
else:
    print("Invalid entry")