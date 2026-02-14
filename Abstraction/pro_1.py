"""Q1: Shape Hierarchy
Abstract class Shape → abstract methods area() and perimeter()
Implement Circle, Rectangle, Triangle
Function to calculate total area and perimeter of a list of shapes"""


#from abc import ABC, abstractmethod
"""ABC → marks a class as abstract
@abstractmethod → marks a method that must be implemented by child classes"""
import math
from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass    

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*self.r**2
    def perimeter(self):
        return  2*math.pi*self.r  


class Rectangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def area(self):
        return self.a*self.b
    def perimeter(self):
        return  2*(self.a+self.b) 


class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=((self.a+self.b+self.c)/2)
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perimeter(self):
        return  ((self.a+self.b+self.c)) 

# Now using these
obj=Triangle(2,3,4)
result=obj.perimeter()
print(result,"Area:",obj.area())




    # Abustract:
""" 🔹 Abstract Class in Python
1️ Meaning (Simple Words)

An abstract class is a blueprint for other classes:

You cannot create objects of an abstract class directly

It defines what methods a class should have, but not how they work

Child classes must implement the abstract methods

✅ Think of it as a plan or template for other classes"""