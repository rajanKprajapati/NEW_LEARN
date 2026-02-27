"""Build a mini project structure:
School
Teacher
Student
Rules:
School has teachers (aggregation)
Student has id_card (composition)
Implement relationships properly."""

class Teacher:
    def __init__(self,tname):
        self.tname=tname
    def teach(self):
        print(f"{self.tname} is teaching")    
class School:
    def __init__(self,teacher):
        self.teacher=teacher #Agreegration
    def check_class(self):
        self.teacher.teach()
        print("Students are studing")
class id_card:
    def id_card(self):
        print(f"Having ID-card")
class Student:
    def __init__(self,name):
        self.name=name
        self.id_card=id_card() #Composition
    def check_Attendence(self):
        print(f"{self.name} is present,")
        self.id_card.id_card()
t1=Teacher("Bhola sir")
s1=School(t1)
s1.check_class()
print("The ....................next.............. one")
st1=Student("Ramu")
st1.check_Attendence()
    