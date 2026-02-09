"""Create class A and B both have method display().
Child class C(A, B) calls display() and print MRO.
Then change order C(B, A) and check output difference."""



class A:
    def display(self):
        print("A")
        # super().display()

class B:
    def display(self):
        # super().display()
        print("B")

class C(A,B):
    def __init__(self):
        pass


obj=C()
print("Change the oder of the A and B after the first output:\n",C.mro()) #mro is print as like this 
obj.display()



"""class A:
    def display(self):
        print("A")
        super().display()

class B:
    def display(self):
        super().display()
        print("B")

class C(A,B):
    def __init__(self):
        pass

obj = C()
print(C.mro())
obj.display()
1️⃣ What super() Does in Multiple Inheritance
super() does not necessarily mean “parent class”, it means the next class in the MRO.

Python uses the Method Resolution Order (MRO) to decide which method super() calls.

2️⃣ MRO of C(A, B):
python
Copy code
C.mro()  # [C, A, B, object]
When you call obj.display():

A.display() is called first.

Inside A.display(), you call super().display().

According to MRO, super() from A → next class is B → calls B.display().

Inside B.display(), you call super().display().

According to MRO, super() from B → next class is object → calls object.display().

3️⃣ The Problem
object does not have a display() method.

So when Python tries to call super().display() from B, it fails → raises AttributeError:

pgsql
Copy code
AttributeError: 'super' object has no attribute 'display'
4️⃣ How to Fix It
You have two main options:

Option 1: Stop at the end
python
Copy code
class A:
    def display(self):
        print("A")
        super().display()

class B:
    def display(self):
        print("B")  # No super() here, stop at the last class

class C(A,B):
    pass

obj = C()
obj.display()
Output:

css
Copy code
A
B
Now it works because B.display() no longer calls super(), so it doesn’t try to call object.display().

"""