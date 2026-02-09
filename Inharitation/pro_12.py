"""Create Teacher and Singer classes.
Child class Person(Teacher, Singer) should use both methods"""

class Teacher:
    def class_teacher(self):
        print("I can Teach")


class Singer:
    def class_singer(self):
        print("I can sing")


class Person(Teacher,Singer):
    pass        

#Creating an object
Ram=Person()
Ram.class_teacher()
Ram.class_singer()
