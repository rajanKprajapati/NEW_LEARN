"""Create Device -> Mobile -> Smartphone

Device has power_on()

Mobile has call()

Smartphone has internet()
Also override power_on() in Smartphone."""

class Device:
    def __init__(self,device_name):
        self.device_name=device_name

    def power_on(self):
        print(f"{self.device_name} is on")

class Mobile(Device):
    def __init__(self,device_name,version):
        super().__init__(device_name)
        self.version=version

    def call(self):
        print(f"{self.device_name} {self.version} is now calling")

class Smartphone(Mobile):
    def __init__(self,device_name,version):
        super().__init__(device_name,version)

    def power_on(self):
        super().power_on()
# IS for:
# ✅ Calling parent methods inside a child method
# ✅ Method overriding
# ✅ Constructor chaining
# ✅ Cooperative multiple inheritance
# ✅ MRO-based call flow
        print(f"{self.device_name} {self.version} is on")
             

#creating an object of this
obj=Smartphone("Samsung","Ultra pro 24.1")
obj.power_on()
obj.call()





# explain these all with examples: super() IS for:
#     ✅ Calling parent methods inside a child method
#     ✅ Method overriding
#     ✅ Constructor chaining ✅ Cooperative multiple inheritance 
#     ✅ MRO-based call flow
"""1️⃣ Calling parent methods inside a child method
👉 Meaning:

When a child class overrides a method, but still wants to use the parent’s version of that method.

Example:
class Parent:
    def show(self):
        print("Parent show")

class Child(Parent):
    def show(self):
        super().show()          # call Parent method
        print("Child show")     # extend behavior

c = Child()
c.show()

Output:
Parent show
Child show

🧠 Concept:

Child is not replacing parent logic — it is extending it.

2️⃣ Method overriding
👉 Meaning:

Child defines same method name as parent to change behavior.

Example:
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")


Without super():

c = Car()
c.start()


Output:

Car starts with key


With super():

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starts with key")


Output:

Vehicle starts
Car starts with key

🧠 Concept:

Override = change
super() = reuse + extend

3️⃣ Constructor chaining
👉 Meaning:

Calling parent constructors so that all parent classes initialize properly.

Example:
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

class C(B):
    def __init__(self):
        super().__init__()
        print("C init")

obj = C()

Output:
A init
B init
C init

🧠 Concept:

Every class gets initialized in proper order
This is constructor chaining

4️⃣ Cooperative multiple inheritance
👉 Meaning:

All parent classes cooperate in method execution using super()
(no class is skipped)

Example:
class A:
    def show(self):
        print("A")
        super().show()

class B:
    def show(self):
        print("B")
        super().show()

class C:
    def show(self):
        print("C")

class D(A, B, C):
    def show(self):
        print("D")
        super().show()

d = D()
d.show()

Output:
D
A
B
C

🧠 Concept:

Each class calls super()
So everyone gets executed
This is called cooperative inheritance

5️⃣ MRO-based call flow (Method Resolution Order)
👉 Meaning:

super() does NOT mean "parent class"
It means next class in MRO order

Example:
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    def show(self):
        super().show()
        print("C")

c = C()
c.show()

MRO:
print(C.mro())

[C, A, B, object]

Output:
A
C


Because super() goes to next in MRO, not necessarily logical parent.

🧠 One-line meanings (Memory version)
Concept	Meaning
Parent method call	Reuse parent logic
Method overriding	Change behavior
Constructor chaining	Init all parents
Cooperative inheritance	All classes participate
MRO-based flow	Next class in order
🎯 Super() Mental Model
❌ Wrong model:

super() = parent class

✅ Correct model:

super() = next class in MRO chain

🧭 Final Truth

super() is not a function.
super() is a navigation system inside inheritance hierarchy.

It controls:

flow

order

execution

cooperation

structure

"""