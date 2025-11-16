class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
        super().show()
class C(A):
    def show(self):
        print("Class C")
        super().show()
class X:
    def show(self):
        print("Class X")
        super().show() # Here X does not have any parent class so commented, so output will be D->B->Y->X due to it will breack the chain
        # If we uncomment the above line then output will be D->B->Y->X->C->A
class Y(X):
    def show(self):
        print("Class Y")
        super().show()
class D(B,Y,C):
    def show(self):
        print("Class D")
        super().show()
        print("MRO for D:", D.__mro__)
d = D()
d.show()