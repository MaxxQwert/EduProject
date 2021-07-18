from VehicleABC import VehicleABC
from VehicleErrors import *


class Vehicle(VehicleABC):

    def __init__(self, volume_tank=0, fuel_cons=0.0, carrying=0, passenger=0, type_vh='', type_eng=''):
        self.type_vh = type_vh
        self.type_eng = type_eng
        self.volume_tank = volume_tank
        self.fuel_cons = fuel_cons
        self.carrying = carrying
        self.passenger = passenger
        self.volume_fuel = 0
        self.status_engine = False

    def buzz(self):
        print(f'{self.type_vh} gives a signal')

    def start_engine(self, status: bool) -> bool:
        if (not self.status_engine) and (not status):
            raise VehicleError('Already stopped')
        elif self.status_engine and status:
            raise VehicleError('Already started')
        elif self.volume_fuel == 0:
            raise VehicleError('The tank is empty')
        self.status_engine = True
        print(f'Engine is started, value of fuel {self.volume_fuel} l')
        return True

    def refuel(self, val: int) -> int:
        if val + self.volume_fuel > self.volume_tank:
            raise VehicleError('Overflow tank')
        self.volume_fuel += val
        print(f'The tank is filled successfully, the volume of fuel in the tank {self.volume_fuel}')
        return self.volume_fuel

    def draw(self, val: int) -> bool:
        if self.volume_fuel == 0:
            raise VehicleError('The tank is empty')
        elif not self.status_engine:
            raise VehicleError('Engine not running')
        self.volume_fuel -= self.fuel_cons * val
        print(
            f'The {self.type_vh} has successfully moved {val} km, the remaining fuel in the tank {self.volume_fuel} l')
        return True


class Car(Vehicle):
    def __init__(self, volume_tank, fuel_cons, carrying, passenger):
        super().__init__(volume_tank, fuel_cons, carrying, passenger)
        self.type_vh = 'Car'
        self.type_eng = 'Benzine'


class Truck(Vehicle):
    def __init__(self, volume_tank, fuel_cons):
        super().__init__(volume_tank, fuel_cons)
        self.type_vh = 'Truck'
        self.type_eng = 'Diesel'

    def dump_truck(self):
        print('Body raised')


class Airplanes(Vehicle):
    def __init__(self, volume_tank, fuel_cons, carrying, passenger):
        super().__init__(volume_tank, fuel_cons, carrying, passenger)
        self.type_vh = 'Airplanes'
        self.type_eng = 'Kerosene'


class Sailboat(Vehicle):
    def __init__(self, carrying: int, passenger: int):

        super().__init__(carrying, passenger)

        self.type_vh = 'Sailboat'
        self.type_eng = 'Sail'
        self.volume_tank = 0
        self.status_sail = False

    def sail_open(self, status: bool) -> bool:
        if (not self.status_sail) and (not status):
            raise VehicleError('Already stopped')
        elif self.status_sail and status:
            raise VehicleError('Already started')
        self.status_sail = True
        print(f'Sail is open')
        return True

    def draw(self, val: int) -> bool:
        if not self.status_engine:
            raise VehicleError('Engine not running')
        print(
            f'The {self.type_vh} has successfully moved {val} km')
        return True
