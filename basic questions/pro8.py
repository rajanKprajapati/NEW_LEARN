"""Create a class Math with a @staticmethod square(n) that returns square of number.
Test it using:"""
class Math:
    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(12,13)) #there is no need of 'cls' variable
obj=Math()
print(obj.add(12,23)) # there is not need of "self" variable in creation of the function this the class Math 
