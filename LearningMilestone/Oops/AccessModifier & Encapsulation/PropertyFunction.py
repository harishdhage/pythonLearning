
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
    name = property(get_name,set_name,'name') # creating property for name
    age = property(get_age,set_age,'age')

e1 = Employee('Kariya', 12)
print(f'Name - {e1.name} and age - {e1.age}')
e1.name = 'Dogesh'
e1.age = 21
print(f'Name - {e1.name} and age - {e1.age}')
e1.set_name('Dhage')
e1.set_age(25)
print(f'Name - {e1.name} and age - {e1.age}')