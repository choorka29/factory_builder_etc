from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Motorcycle(Vehicle):
    def drive(self):
        print("Riding a motorcycle")

class VehicleFactory():
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "motorcycle":
            return Motorcycle()
        else:
            raise ValueError("Invalid vehicle type")

vehicle_type = input("Enter vehicle type (car or motorcycle): ")
vehicle = VehicleFactory.create_vehicle(vehicle_type)
vehicle.drive()