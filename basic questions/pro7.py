class Student:
    collage="Biet" # calss variable

    def __init__(self,name):
        self.name=name # instance variable

# changing the class varialble 'to the class name'
Student.collage="Rameshwaram"   

s1=Student("Haariom")
s2=Student("Mukesh")
# If I will do as 
s1.collage="SR institute" #Then the class variable become instance variable for s1 object
print(f"Collage name in which both student are stuied:{s1.collage} as same as {s2.collage}")
print(f"Student 1st:{s1.name}, 2nd:{s2.name}")

 

