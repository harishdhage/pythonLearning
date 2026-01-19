class Employee:
    def __init__(self, name, age):
        self.__name = name # private
        self.__age = age # private
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age

e1 = Employee('Kariya', 12)
print(f'Name - {e1.get_name()} and age - {e1.get_age()}')
e1.set_name('Dhage')
e1.set_age(25)
print(f'Name - {e1.get_name()} and age - {e1.get_age()}')
e2 = Employee('Puppy', 30)
print(f'Name - {e2.get_name()} and age - {e2.get_age()}')
Employee.set_name(e1, 'Circuit')
Employee.set_age(e1, 39)
print(f'Name - {Employee.get_name(e1)} and age - {Employee.get_age(e1)}')