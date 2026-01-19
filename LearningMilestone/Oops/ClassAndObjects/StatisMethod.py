
class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def getInfo(self):
        print(f" {self.name} : {self.position}")

    @staticmethod
    def checkposition(position): # static method
        valid_position = ['Manager', 'HR', 'Electrician', 'Cook']
        return position in valid_position

emp1 = Employee('Dogesh', 'HR')
emp2 = Employee('Rogesh', 'Cook')
print("Is it valid position : ",Employee.checkposition('Client'))
emp2.getInfo()
print("Is it valid position : ",emp1.checkposition('HR'))