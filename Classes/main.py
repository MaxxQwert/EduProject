from abc import ABCMeta, abstractmethod


class VehicleABC(metaclass=ABCMeta):

    @abstractmethod
    def Buzz(self):
        raise NotImplementedError

    @abstractmethod
    def start_engine(self, status: bool) -> bool:
        raise NotImplementedError

    @abstractmethod
    def refuel(self, val: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def draw(self, val: int) -> int:
        raise NotImplementedError


class Vehicle(VehicleABC):

    def __init__(self, type_vh, type_eng, volume_tank, fuel_cons, carrying, passenger):
        self.type_vh = type_vh
        self.type_eng = type_eng
        self.volume_tank = volume_tank
        self.fuel_cons = fuel_cons
        self.carrying = carrying
        self.passenger = passenger
        self.volume_fuel = 0
        self.status_engine = False

    def Buzz(self):
        print(f'{self.type_vh} gives a signal')

    def start_engine(self, status: bool):
        if self.volume_fuel == 0:
            raise Exception('Not enough fuel')


class Car(Vehicle):
    def vroom(self):
        print("Cars go vroom vroom")


class Cooper(Car):
    def drift(self):
        print("Mini Coopers can drift well")


class Airplanes(Vehicle):
    def fly(self):
        print("weeeeee I'm flying")


class Tank(Vehicle):
    # custom init because tanks have guns!~
    # taking the gun size and tossing the rest of the arguments to the parent.
    # if the parent doesn't find a __init__ it will keep going up until one is found or unelss we call it.
    # Here we made a new __init__ so it doesn't go looking for one, but we call super() which is calling for the
    # parent's __init__
    def __init__(self, gun_size, *args):
        self.gun_size = gun_size
        super(Tank, self).__init__(*args)

    def fire(self):
        print("pew pew pew")

    # I have my custom get_stats but still calls parent's one so I don't repeat code.
    def get_stats(self):
        print("my gun is this big: %d " % self.gun_size)
        super(Tank, self).get_stats()


a = Cooper(150, 150, "blue", 4)
a.drift()
a.vroom()
a.honk()
a.get_stats()
print(a.number_of_vehicles)

b = Airplanes(200, 150, "white", 2)
b.fly()
print(b.number_of_vehicles)

c = Tank(500, 500, 250, "Green", 18)
c.fire()
print(c.number_of_vehicles)
c.get_stats()
