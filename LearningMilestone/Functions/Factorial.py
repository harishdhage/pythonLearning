
def factorialNum(num):
    if num <= 1:
        return 1
    else:
        return num * factorialNum(num-1)

print(factorialNum(6))

