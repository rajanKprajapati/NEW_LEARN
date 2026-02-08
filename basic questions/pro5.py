class Numbers:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def calculate(self):
        return self.num1+self.num2,self.num1-self.num2
        # return f"sum:{self.num1+self.num2},differ:{self.num1-self.num2 if self.num1>self.num2 else self.num2-self.num1}"
choice="yes"
while choice=="yes":
    a,b=int(input("a=")),int(input("b="))
    obj1=Numbers(a,b)
    num1,num2=obj1.calculate()
    print("sum=",num1,"differ=",num2)
    choice=input("Enter Choice:")
   
