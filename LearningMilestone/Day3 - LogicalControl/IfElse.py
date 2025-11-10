hieght = int(input("Enter your hieght in cm to ride roller coaster : "))
bill = 0
if hieght > 120 :
    print("You can ride!")

    age = int(input("Enter your age : "))
    if age <= 12:
        bill = 5
        print("Ticker price : $5")
    elif age <= 16:
        bill = 10
        print("Ticket price : $10")
    else:
        bill = 20
        print("Ticket price : $20")
    want_photo=input("Do you want to take photo? y for yes and n for no : ")
    if want_photo=='y':
        bill += 3
    print(f"Your final bill : {bill}")
else:
    print("Not eligable")