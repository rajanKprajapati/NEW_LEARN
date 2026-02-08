"""Create class Vehicle with start() and stop().
Create class Car(Vehicle) and override start() to print "Car starts with key"."""


class Vehicle:
    # def __init__(self):
    def start(self):
        print("Car is start")

    def stop(self):
        print("Car is stop")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#creating an object
obj=Car()
obj.start()#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< that's the main reason the super is used
 

# /////////////////////////////////////////////////////
"""Exact currect answer"""
# class Vehicle:
#     def start(self):
#         print("Vehicle starts")

#     def stop(self):
#         print("Vehicle stops")

# class Car(Vehicle):
#     def start(self):
#         print("Car starts with key")

# obj = Car()
# obj.start()
# obj.stop()
# ///////////////////////////////////////////////////////////////



#below Examples and output is enough to understand


"""Why super() is important in multiple inheritance?
First understand Multiple Inheritance

Multiple inheritance means:

👉 One child class has more than 1 parent class

Example:

class A:
    pass

class B:
    pass

class C(A, B):   # C has 2 parents
    pass


So question is:

❓ If both parents have a method show(), then which one should run first?

That’s why Python uses MRO.

✅ What is MRO (in very simple words)?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

MRO = Method Resolution Order

It means:

✅ Python has a fixed order to search methods.

Example:

class C(A, B):
    pass


Then Python searches like this:

👉 C → A → B → object<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

So if you call:

c.show()


Python checks:

C.show()

A.show()

B.show()

object.show()

❌ Problem when you call parent method directly

Suppose we do this:

A.show(self)


This means:

🚫 You are forcing Python:
👉 “Call A only, ignore MRO order”

So Python MRO chain breaks.

✅ Best Example (Very easy to understand)
❌ Without super() (problem)
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    def show(self):
        A.show(self)   # forced call
        B.show(self)   # forced call
        print("C")

obj = C()
obj.show()

Output:
A
B
C


Here it looks okay, but in real cases parents also call show() further, then problem happens.

✅ Real Multiple Inheritance Problem (Important)
❌ Wrong way (Direct parent calling causes duplication)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        A.show(self)
        print("B")

class C(A):
    def show(self):
        A.show(self)
        print("C")

class D(B, C):
    def show(self):
        B.show(self)
        C.show(self)
        print("D")

obj = D()
obj.show()

Output:
A
B
A
C
D


⚠️ See the problem?

👉 A printed 2 times
Because you manually called A from both B and C.

This is the meaning of:

❌ “Some methods may run twice”

✅ Correct way using super() (Best way)
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(A):
    def show(self):
        super().show()
        print("C")

class D(B, C):
    def show(self):
        super().show()
        print("D")

obj = D()
obj.show()

Output:
A
C
B
D


✅ Now everything runs only once
✅ In correct order (MRO order)

⭐ Final Simple Meaning of super()
You said:

super() does NOT mean “call parent only”

YES ✅

Real meaning:

✅ super() means:

👉 Call the NEXT class method in MRO order

Not directly parent.

🧠 One line summary

✅ super() is important in multiple inheritance because it follows MRO order automatically and prevents method duplication or skipping."""