"""
Transportation Factory:
Build a TransportationFactory to generate instances of transportation vehicles (Car, Bike, Bus) depending on user requirements.
"""

from abc import ABC, abstractmethod

class TransportationFactory(ABC):
    @abstractmethod
    def create_transport(self, name):
        pass

class Vehicle(TransportationFactory):
    def __init__(self, name):
        self.name = name

    def display_info(self):
        pass

class Car(Vehicle):
    def display_info(self):
        print(f"This is a car with name {self.name}")

class Bike(Vehicle):
    def display_info(self):
        print(f"This is a bike with name {self.name}")

class Bus(Vehicle):
    def display_info(self):
        print(f"This is a bus with name {self.name}")

class TransportationFactoryImpl(TransportationFactory):
    def create_transport(self, transport_type, name):
        if transport_type == "car":
            return Car(name)
        elif transport_type == "bike":
            return Bike(name)
        elif transport_type == "bus":
            return Bus(name)
        else:
            raise ValueError("Invalid transportation type")

def main():
    factory = TransportationFactoryImpl()

    car = factory.create_transport("car", "Sedan")
    bike = factory.create_transport("bike", "Mountain Bike")
    bus = factory.create_transport("bus", "City Bus")

    vehicles = [car, bike, bus]
    for vehicle in vehicles:
        vehicle.display_info()

if __name__ == "__main__":
    main()
