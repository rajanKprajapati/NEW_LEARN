"""Create A -> B -> C
Each class has constructor printing its class name.
Use super() to call constructors properly.
"""

class A:
    def __init__(self):
        print("Class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("class B")

class C(B) :
    def __init__(self):
        super().__init__()
        print("class C")  


#creating an obj
obj=C()
print(C.mro())



# 🔍 What is MRO?
# MRO = Method Resolution Order
"""
It tells Python:

“When a method is called, in which order should I check the classes?”

🧠 Structure of MRO list

Example:

print(C.mro())


Output:

[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


Meaning:

C → A → B → object

🎯 How Python uses this list

When you do:

obj.show()


Python does:

1️⃣ Look in C
2️⃣ If not found → look in A
3️⃣ If not found → look in B
4️⃣ If not found → look in object
5️⃣ If not found → error

🔁 MRO in multiple inheritance
class C(A, B):


Order matters:

class C(A, B):  # A first


MRO:

C → A → B → object

class C(B, A):  # B first


MRO:

C → B → A → object

🧬 Why MRO exists

Because of:

multiple inheritance

method name conflicts

ambiguity

diamond problem

predictable execution

safe inheritance

🧠 Mental model

Think of MRO as:

A road map Python follows to find methods.

🔥 Relation with super()

super() uses MRO:

super().show()


Means:

Go to next class in MRO list, not parent class.

🏆 One-line definition

MRO list is the linear order of classes Python follows to resolve method calls.

🎯 Simple language

Python class resolution ka route hota hai MRO.

🧭 Real-world analogy

Like Google Maps route:

Home → Road1 → Road2 → Destination


MRO:

Class → Parent1 → Parent2 → object

🧠 Interview answer

MRO (Method Resolution Order) is the order in which Python looks for a method in a class hierarchy. Python uses C3 linearization algorithm to generate this order, ensuring consistent and predictable method resolution.

🔥 Summary
Point	Meaning
MRO	Search order
Used for	Method lookup
Applies to	Inheritance
Handles	Conflicts
Algorithm	C3 linearization
super()	Follows MRO
object	Always last
Final line:

MRO list explains how Python decides which method to execute."""


# ❓ What is class 'object'?
# 👉 object is the root class of all classes in Python.
"""
In Python:

Every class automatically inherits from object.

Even if you don’t write it.

🧠 Meaning of the list

This list means:

C → A → B → object


So Python will search:

1️⃣ Class C
2️⃣ Class A
3️⃣ Class B
4️⃣ Class object (built-in root class)

🧬 What is object class?

It is Python’s base class.

It provides core features like:

__init__

__str__

__repr__

__eq__

__hash__

__class__

__dir__

__sizeof__

memory handling

identity handling

🎯 Why is object always last?

Because it is the top-most ancestor in Python’s class hierarchy.

Hierarchy:

object
  ↑
  A
  ↑
  B
  ↑
  C


(logical representation reversed in MRO list)
🧠 Mental Model
Think like a tree:
        object
          |
         A
          |
         B
          |
         C


Python always ends at object.

🔥 Why this matters

Because:

Every class is an object

Everything in Python is an object

All features come from object

Python is fully object-oriented

🎯 Simple language:

object is Python’s default parent class.

🏆 One-line definition:

object is the ultimate base class of all Python classes.

🧭 Interview Answer:

In Python, all classes implicitly inherit from the built-in object
 class, which is why object always appears at the end of the MRO list.
"""





