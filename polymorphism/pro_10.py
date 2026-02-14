"""Create a Student class with name and marks. Overload:
+ → add marks of two students → return a new student with combined marks.
== → compare marks of two students.
> → check if first student has more marks.
print() → print in format: "Name: xxx, Marks: yyy"""

class Student:
    def __init__(self,Name,Marks):
        self.Name=Name
        self.Marks=Marks

    def __add__(self,other):
        name=self.Name+"&"+other.Name 
        marks=self.Marks+other.Marks
        return Student(name,marks) 
    
    def __eq__(self,other ):
        return self.Marks==other.Marks
    
    def __gt__(self,other):
        return self.Marks>other.Marks
           

    def __str__(self):
        return  f"Name:{self.Name},Marks:{self.Marks}" 


obj1= Student("Rajan",15)
obj2=Student("Mithilesh",14)     
obj=obj1+obj2
print(obj)    
print(obj1>obj2)
print(obj1==obj2)



"""What Vector(...) really is
Vector(self.x + other.x, self.y + other.y)


Vector here is the class name.

Using Vector(...) creates a new object of type Vector.

The constructor __init__ is automatically called with the values you pass:

def __init__(self, x, y):
    self.x = x
    self.y = y


So in this line:

Vector(self.x + other.x, self.y + other.y)


Adds x and y components

Creates a new Vector object with those values

Returns that object from __add__()

2️⃣ How __str__() comes into play

When you do:

v1 = Vector(2,3)
v2 = Vector(4,5)
print(v1 + v2)


Step by step:

v1 + v2 → calls v1.__add__(v2)

__add__() returns a new Vector object:

Vector(6, 8)


print(...) tries to print this object

Python sees an object → calls __str__() of that object automatically

__str__() returns a string:

"(6, 8)"


print() prints that string → (6, 8) ✅

3️⃣ Important Note

Vector(...) does not convert to string.

It only creates an object.

__str__() is what converts an object to a string for printing.

So the flow is:

v1 + v2
  |
  v
__add__() -> returns Vector object
  |
  v
print() -> calls __str__() -> returns string -> printed
"""
