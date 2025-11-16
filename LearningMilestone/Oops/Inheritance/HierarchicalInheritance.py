class Manager:
    def managerInfo(self):
        print("Inside Manager class")

class Employee1(Manager):
    def employee1Method(self):
        print("Inside Employee1")

class Employee2(Manager):
    def employee2Method(self):
        print("Inside Employee2")

e1 = Employee1()
e2 = Employee2()
e1.employee1Method()
e1.managerInfo()
e2.employee2Method()
e2.managerInfo()
