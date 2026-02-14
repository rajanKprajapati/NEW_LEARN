"""Create Bird, Plane, Drone classes all with fly() method and use one function to call them."""

class Bird:
    def fly(self):
        print("Bird can fly")
class Plane:
    def fly(self):
        print("Plane can fly")
class Drone:
    def fly(self):
        print("Drone can fly")

def call_function(objs):
    for i in objs:
        i.fly()

objs=[Bird(),Plane(),Drone()]
call_function(objs)        


