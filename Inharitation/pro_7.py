"""Create Person -> Student -> CollegeStudent
Add one method in each class and call all from CollegeStudent."""

class Person:
    def method1(self):
        print("this is the method1")

class Student(Person):
    def method2(self):
        print("this is the method2")

class CollageStudent(Student):
    def method3(self):
        print("this is the method3")

#creating an object:
obj=CollageStudent()
obj.method1()
obj.method2()
obj.method3()               