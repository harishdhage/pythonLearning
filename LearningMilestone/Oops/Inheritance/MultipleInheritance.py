class Vehicle:
    def feature(self,seatingCapacity=2):
        print('Its Bike')
    def displayVehicle(self):
        print("From Vehicle class")
class Car(Vehicle):
    def feature(self,seatingCapacity=4):
        if seatingCapacity ==4:
            print('Its Car')
        elif seatingCapacity == 7:
            print('Its SUV')
    def displayCar(self):
        print("From Car class")
class Bus(Car):
    def feature(self,seatingCapacity=20):
        if seatingCapacity == 20:
            print('Its Mini Bus')
        elif seatingCapacity == 51:
            print('Its Big Bus')
    def displayBus(self):
        print("From Bus class")

b1 = Bus()
b1.feature(20)
b1.displayVehicle()
b1.displayCar()
b1.displayBus()