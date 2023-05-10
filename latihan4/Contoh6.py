class Wheel:
    def __init__(self, size):
        self.size = size

class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, wheels, engine):
        self.wheels = wheels
        self.engine = engine

wheel1 = Wheel(18)
wheel2 = Wheel(18)
wheel3 = Wheel(18)
wheel4 = Wheel(18)
engine = Engine(150)
car = Car([wheel1, wheel2, wheel3, wheel4], engine)
print(car.wheels[0].size)
