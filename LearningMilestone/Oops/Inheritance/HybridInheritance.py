class Ceo:
    def ceoMethod(self):
        print("Inside CEO class")
class Manager(Ceo):
    def managerMethod(self):
        print("Inside Manager info")

class Apple:
    def appleMethod(self):
        print("Inside Apple class")
class Employee1(Manager):
    def employee1method(self):
        print("Inside Employee1")
#class Employee2(Ceo,Manager): # Parameter should follow the class defined hierchy, need to start from leaf to root
class Employee2(Manager,Ceo):
    def employee2method(self):
        print("Inside Employee2")
class InheritClass(Apple,Manager,Ceo):
    def inheritMethod(self):
        print("Inside InheritClass")

mgr = Manager()
mgr.managerMethod()
mgr.ceoMethod()
e1=Employee1()
e2=Employee2()
e1.employee1method()
e1.managerMethod()
e1.ceoMethod()
e2.employee2method()
e2.managerMethod()
e2.ceoMethod()
i1 = InheritClass()
i1.appleMethod()
i1.inheritMethod()
i1.ceoMethod()
i1.managerMethod()