"""Q1.

Create a class Student with:

public variable: name

public method: show_name()
Print the name using both variable and method."""

class Student:
    def __init__(self,name):
        self.name=name

    def show_name(self):
        print("Name:",self.name)

s1=Student("Monu")
print(f"By public variable name:\nName:{s1.name}")           
print("By method:")
s1.show_name()