class ParentClass:
    def parentMethod(self):
        print("From Parent")

class ChildClass(ParentClass):
    def childMethod(self):
        print('From Child')

c1=ChildClass()
c1.childMethod()
c1.parentMethod()
p1 = ParentClass()
p1.parentMethod()
#p1.childMethod() # Child class members are not visible to parent, it's invalid call