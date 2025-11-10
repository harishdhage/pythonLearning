
def printDetails(**krargs): #Keyword argument start with 2 * sign
    for key,value in krargs.items():
        print(f"{key}:{value}")

printDetails(name='Nimbu',age=23,address='12/3 Os,Villa')

def combinedFunc(*args, **kwargs):
    for val in args:
        print(f'Positional Argument : {val}')
    for key,value in krargs.items():
        print(f"{key}:{value}")

combinedFunc(1,6,2,5.2,True,'Mango',name='Nimbu',age=23,address='12/3 Os,Villa')