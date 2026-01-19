class Father:
    def skill(self):
        print("Father skill is Drinking")
class Mother:
    def skill(self):
        print("Mother skill is Arguing")
class Child(Father, Mother):
    pass

c1 = Child()
c1.skill()