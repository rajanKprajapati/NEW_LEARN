"""Hard 1:
Create Student class with register() method:

only name

name + age

name + age + course"""


class Student:
    def register(self,**data):
        if len(data)==1:
            print("Registered name is:",data["Name"])
        elif len(data)==2:
            print("Registered name is:",data["Name"])
            print("Register age is:",data["Age"]) 
        else:
            print("Registered name is:",data["Name"])
            print("Register age is:",data["Age"])
            print("Register course is:",data["Course"])           

obj=Student()
obj.register(Name="Rajan")
print("")
obj.register(Name="Rajan",Age=21)
print("")
obj.register(Name="Rajan",Age=21,Course="Btech")