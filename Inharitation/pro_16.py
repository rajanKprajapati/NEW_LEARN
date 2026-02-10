"""Create Shape class with method area()
Create Circle(Shape) and Rectangle(Shape) with their own area formulas."""

class Shape:
    def area(self):
        print("Area:")
        
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print(3.14*self.r**2)

class Rectangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        print(self.a*self.b)    

#real use of this
shape=[Circle(2),Rectangle(12,5)]

for s in shape:
    p=s.area()
