from Vehicles import Vehicle, Car, Sailboat, Airplanes, Truck
from VehicleErrors import VehicleError

vehicles = Vehicle(100, 0.1, 300, 8, 'Super Car', 'Benzine')
try:
    vehicles.start_engine(True)
except VehicleError as err:
    print(err)
try:
    vehicles.refuel(200)
except VehicleError as err:
    print(err)
vehicles.refuel(80)
vehicles.start_engine(True)
try:
    vehicles.start_engine(True)
except VehicleError as err:
    print(err)
try:
    vehicles.draw(100)
except VehicleError as err:
    print(err)

vehicles = Sailboat(10, 500)
try:
    vehicles.sail_open(True)
except VehicleError as err:
    print(err)
try:
    vehicles.refuel(200)
except VehicleError as err:
    print(err)


try:
    vehicles.start_engine(True)
except VehicleError as err:
    print(err)
try:
    print('Drawing Sailboat')
    vehicles.draw(100)
except VehicleError as err:
    print(err)
car = Car(80, 0.05, 200, 5)
air = Airplanes(800, 200, 10000, 2)
truck = Truck(300, 2)
truck.dump_truck()
car.refuel(80)
car.start_engine(True)
print(car.status_engine)
print(car.volume_fuel)
car.draw(10)
print(car.volume_fuel)
car.buzz()
print(car)
