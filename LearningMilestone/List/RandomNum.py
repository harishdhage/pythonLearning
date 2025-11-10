import random
randomNum = random.randint(25, 125)
print(randomNum)
randomNum = random.random() #To generate floating num
print(randomNum)
randomNum = random.uniform(25, 125)
print(randomNum)
randomNum = random.randint(0, 1)
if randomNum==0:
    print("Heads")
else:
    print("tails")