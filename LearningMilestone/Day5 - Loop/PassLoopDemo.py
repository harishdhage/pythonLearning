for i in range(1, 10):
    if i == 3:
        print("Skip")
        pass
        print("After pass in For loop")
    print(i)

count = 0
while count<15:
    if count == 5:
        print("Skip 5")
        count = count+1
        pass
        print("After pass in while loop")
    print(count)
    count = count+1
