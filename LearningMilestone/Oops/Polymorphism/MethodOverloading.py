class SomeClass:
    #Below code will throw TypeError
    '''
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
    '''
    #Fix aboev code
    def add(self,a=None,b=None,c=None):
        x=0
        if a != None and b != None and c != None:
            x = a+b+c
        elif a != None and b != None and c == None:
            x = a+b
        return x
sc = SomeClass()
print(sc.add(2,3,5))
print(sc.add(2,3))
