class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_model(self, model):
        self.car.model = model

    def set_color(self, color):
        self.car.color = color

    def set_wheels(self, wheels):
        self.car.wheels = wheels

    def get_result(self):
        return self.car

class Car:
    def __init__(self):
        self.model = None
        self.color = None
        self.wheels = None

    def __str__(self):
        return f"{self.color} {self.model} with {self.wheels} wheels"

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self, model, color, wheels):
        self.builder.set_model(model)
        self.builder.set_color(color)
        self.builder.set_wheels(wheels)
        return self.builder.get_result()

car_builder = CarBuilder()
director = Director(car_builder)
car = director.construct_car("Toyota", "blue", 4)
print(car)