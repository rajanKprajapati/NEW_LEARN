"""Create class Employee with name, salary.
Create class Developer(Employee) with language. Print all details."""

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


class Developer(Employee):
    
    def __init__(self,name,salary,language):
        super().__init__(name,salary)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.language=language 


#printing all details
obj=Developer("ram","200000","python")
print(f"Name:{obj.name}\n Salary:{obj.salary}\n Language:{obj.language}")   



"""✅ Use of super() (Why we use it?)

super() is used to call the parent class methods or constructor from the child class.

⭐ 1) Call Parent Class Method (Most common use)

If child class overrides a method, but you still want to use the parent’s method also:

class Parent:
    def show(self):
        print("Parent show")

class Child(Parent):
    def show(self):
        super().show()   # calling parent method
        print("Child show")

c = Child()
c.show()


✅ Output:

Parent show
Child show

⭐ 2) Call Parent Class Constructor (__init__)

When child class has its own constructor but you also want to run parent constructor:

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()   # calling parent constructor<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        print("Child constructor")

c = Child()


✅ Output:

Parent constructor
Child constructor

⭐ 3) Helps in Multiple Inheritance (Very important)

In multiple inheritance, super() helps Python follow the correct order (MRO = Method Resolution Order).

✅ Simple Meaning
super() = Parent class ka reference

So you can reuse parent class code inside child class."""