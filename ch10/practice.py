print("1---------")
import random
clovers = ['clover1','clover2','clover3']
print(random.sample(clovers,2))

print("2---------")

class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class Bicycle(Car):
    def __init__(self, year, wheel, price, name):
        super().__init__(wheel, price)
        self.year = year
        self.name = name

    def drivetrain(self):
        print(self.name) 

    def info(self):
        print("year :",self.year,"\nwheel :",self.wheel,"\nprice :",self.price,"\ndrivetrain :",self.name)

car = Car(4,3000)
print(car.wheel)
print(car.price)

bicycle = Bicycle(2021, 2, 100, "시마노") 
print(bicycle.year) 
print(bicycle.wheel)
print(bicycle.price) 
bicycle.drivetrain()
bicycle.info()