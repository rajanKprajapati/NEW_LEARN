"""Create class Animal with method eat().
Create class Dog(Animal) with method bark(). Call both methods."""

class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("Dog is a animal that can bark")
 

#calling both method from the child and parent both 
obj=Dog()
obj.eat()
obj.bark()
print("THis is the result") 