class Employee:
    def __init__(self, name, age, sex):
        self.name = name # public
        self._age = age # protected
        self.__sex = sex # private
    def displaydetails(self):
        print(f'Name - {self.name} | age - {self._age} | sex - {self.__sex}')

e1 = Employee('Kariya', 12, 'M')
e1.displaydetails()
print(e1.name)
print(e1._age)
print(e1._Employee__sex) # This is how we can access private variable outside the class using name mangling