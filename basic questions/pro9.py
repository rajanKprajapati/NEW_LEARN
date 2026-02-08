"""Create a class Student with:

class variable college = "ABC"

@classmethod change_college(new_name) to update college name
Then print updated college."""

class Student:
    collage="BIET"
    @classmethod
    def change_collage(cls,new_name):
        cls.collage=new_name

obj=Student()
print("old collage name:",obj.collage)
obj.change_collage("SRIG")
print("After chnage the collage name......")
print("new collage name:",obj.collage)