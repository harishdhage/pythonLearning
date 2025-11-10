
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

s1 = Student('Chorr', 3.2)
print(f'Name - {s1.name} and gpa - {s1.gpa}')