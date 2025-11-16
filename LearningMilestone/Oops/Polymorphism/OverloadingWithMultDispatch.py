from multipledispatch import dispatch
class SomeClass:
    @dispatch(int,int)
    def add(self,a,b):
        return a+b
    @dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c

sc = SomeClass()
print(sc.add(2,3,5))
print(sc.add(2,3))
