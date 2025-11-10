
class Car:
    'Its car class'
    count=0
    def __init__(self,company, model):
        self.company = company
        self.modl = model
        Car.count+=1
    def suv(self):
        print(f" {self.company} manufactures suv" )
    def countDisplay(self):
        print('Count %d'%Car.count)

car = Car("Tata", "Nexon")
print(car.company ," : ",car.modl)
car.suv()
car.countDisplay()
