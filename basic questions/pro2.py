class Person:
    def __init__(self,name="Unknown",age=0):
        self.name=name
        self.age=age

obj1=Person()
obj2=Person("Rajan",20)
print("obj1 data:",obj1.name,"age:",obj1.age)
print("obj1 data:",obj2.name,"age:",obj2.age)