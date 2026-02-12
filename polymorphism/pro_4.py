"""Create multiply() method that can multiply 2 or more numbers."""
#this is called overloading
""" Python does NOT support traditional overloading like Java
✅ Python uses:

default arguments

*args

**kwargs"""
class Calculation:
    def multiply(slef,*num):
        sum=1
        for i in num:
            sum*=i
        print("Sum=",sum)    

obj=Calculation()
obj.multiply(2,4)
obj.multiply(12,3)
