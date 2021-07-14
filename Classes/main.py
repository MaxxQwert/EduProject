class Vehicle(object):
    #class variable shared between all instances of objects.
    number_of_vehicles = 0

    def __init__(self,length,width,color,wheels):
        self.length = length
        self.width = width
        self.color = color
        self.wheels = wheels
        Vehicle.number_of_vehicles += 1 #increasing class varaible count

    def get_length(self):
        print("I am %d meters long!"%self.length)

    def get_wdith(self):
        print("I am %d meters wide!"%self.width)

    def get_color(self):
        print("My color is %s!"%self.color)

    def get_wheels(self):
        print("I have %d number of wheels"%self.wheels)

    #calling my methods so I don't need to call each of their own
    def get_stats(self):
        self.get_length()
        self.get_wheels()
        self.get_wdith()
        self.get_color()

    def honk(self):
        print("beep beep")

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
    #custom init because tanks have guns!~
    #taking the gun size and tossing the rest of the arguments to the parent.
    #if the parent doesn't find a __init__ it will keep going up until one is found or unelss we call it.
    #Here we made a new __init__ so it doesn't go looking for one, but we call super() which is calling for the
    #parent's __init__
    def __init__(self,gun_size,*args):
        self.gun_size = gun_size
        super(Tank,self).__init__(*args)
    def fire(self):
        print("pew pew pew")

    #I have my custom get_stats but still calls parent's one so I don't repeat code.
    def get_stats(self):
        print("my gun is this big: %d " %self.gun_size)
        super(Tank,self).get_stats()

a = Cooper(150,150,"blue",4)
a.drift()
a.vroom()
a.honk()
a.get_stats()
print(a.number_of_vehicles)

b = Airplanes(200,150,"white",2)
b.fly()
print(b.number_of_vehicles)

c = Tank(500,500,250,"Green",18)
c.fire()
print(c.number_of_vehicles)
c.get_stats()