
class Employee:
    count=1
    nums=10
    def __init__(self, name, salary): # self is the current object
        self.name = name
        self.salary = salary
        self.count+=1
        Employee.nums+=1 # Accessing class variable using class name
    def displayEmployee(self):
        print(f'Employee name : {self.name} and salary : {self.salary}')
    def displayCount(self):
        print('Total employee : %d'%self.count)
        print('Total nums : %d'%Employee.nums)
    def employeeDept(self,dept):
        self.dept = dept
        print(f'Employee : {self.name} work for department : {self.dept}')

emp1 = Employee('Kutta',3000)
emp1.displayCount()
emp2 = Employee('Dogesh', 1000)
emp1.displayEmployee()
emp2.displayEmployee()
emp2.displayCount()
emp1.displayCount()
emp3 = emp1
emp3.displayEmployee()
emp3.displayCount()
emp2.employeeDept("IT")
emp = Employee('Puppy', 5000)
emp.displayCount()
print('Nums : ',Employee.nums)
Employee.nums+=10
print('Nums after increment : ',Employee.nums)

