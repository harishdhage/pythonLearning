
try:
    num = int(input("Enter a number"))
    result = 25/num
except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print(ve)
else:
    print("inside else")
    print(result)
finally:
    print("Inside finally")
