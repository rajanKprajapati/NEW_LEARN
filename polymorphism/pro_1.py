"""Create Animal class with sound() method.
Create Dog, Cat, Cow classes and show polymorphism using a loop."""


class Animal:
    def __init__(self):
        pass

    def sound(self):
        print("Animal is making sound")

class Dog(Animal):
            def sound(self):
                #  super().sound() #not conceptually correct
                 """pure polymorphism, usually:
                    Child replaces parent behavior"""
                 print("barking")
                 


class Cat(Animal):
      def sound(self):
            print("Miauuuu")

class Cow(Animal):
      def sound(self):
            print("bhaaaa")

list=[Dog(),Cat(),Cow()]
for obj in list:
      obj.sound()                       