# Duck Typing — Your Logic (Corrected Form)
"""We create a function that accepts objects, and that function only calls a method name.
Any object that has that method name will work — regardless of class."""

# Question
class Dog:
    def speak(self):
        print("Bark")

class Human:
    def speak(self):
        print("Language English")

class Frog:
    def speak(self):
        print("tercking")


#here obj means "Class_name()"
def take_play(obj):
    obj.speak()

"""importaint library"""
# Addition knowledge 
# obj=Human()
# print(isinstance(obj,Human))   


#now implement the duck type
take_play(Human())

#another call of new class with ssingle function
take_play(Dog())





