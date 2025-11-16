class Parent:
    def __init__(self, name):
        self.name = name
    def displayName(self):
        print(f"Parent class Name - {self.name}")
class Child(Parent):
    def __init__(self, age, name):
        self.age = age
        super().__init__(name)
        #self.name = name
    def displayAge(self):
        print(f"Child class Age - {self.age}")

c1 = Child(21, "Bonda")
c1.displayName()
c1.displayAge()