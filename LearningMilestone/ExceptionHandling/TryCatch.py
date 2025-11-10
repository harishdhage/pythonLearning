
try:
    a=b
except:
    print("var a not assigned")

try:
    a=1/0
except ZeroDivisionError as zde:
    print(zde)
    