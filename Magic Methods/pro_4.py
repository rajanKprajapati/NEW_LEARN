"""Design a system:
Company and Employee
Use aggregation
Employee should exist even without Company
Implement work() method."""

class Employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print(f"{self.name} is working")    

class Compnay:
    def __init__(self,employee):
        self.employee=employee #Agreegration
    def task(self):
        self.employee.work() 
        print("Compnay is now in running condition") 

E1=Employee("Raju")
C1=Compnay(E1)
C1.task()


