class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")


#class D(A,B, C):  #Not allowed to super parent class A
class D(B, C): # Diamond Problem
    pass

d = D()
d.show()