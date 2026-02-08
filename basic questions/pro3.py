class Math:
    def __init__(self,num):
        self.num=num

    def squire(self):
        return self.num**2

    def cube(self):
        return self.num**3
    
surface1=Math(23)
print(surface1.squire())    