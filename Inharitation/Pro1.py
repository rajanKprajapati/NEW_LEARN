#inharitance
class Parants:
    def new(self):
        print("I am parent")

class Child(Parants):
    def new(self):
        super().new() #super() is use to call the parent method into the child method
        print("I am the child of the Parant")


#creating child object
obj1=Child()
obj1.new()
