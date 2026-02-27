"""Design a system:
Human and Heart
Use composition
Heart should not exist without Human
Implement live() method."""


class Heart:
    def live(self):
        print("Heart is breathing")

class Human:
    def __init__(self):
        self.heart=Heart()  #Strong Enter-dependency->Composition
    def live(self):
        self.heart.live()
        print("human is alive")  

man=Human() 
man.live()       