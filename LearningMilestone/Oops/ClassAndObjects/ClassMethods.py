class Students:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count+=1
        Students.total_gpa += gpa
    def displayStudentInfo(self):
        print(f'Name : {self.name} and gpa : {self.gpa}')

    @classmethod
    def totalStudent(cls):
        print(f'Total student : {cls.count}')

    # ttl_stndt = classmethod(totalStudent(cls=Students)) #Above totalStudent is marking as classmethod

    @classmethod
    def getAvgGpa(cls):
        return f'Avg gpa : {cls.total_gpa / cls.count:.2f}' #Here .2f to show only 2 decimal

Students('Madav', 3.4).displayStudentInfo()
s1 = Students('Keshav', 4.4)
s1.displayStudentInfo()
Students.totalStudent()
print(Students.getAvgGpa())