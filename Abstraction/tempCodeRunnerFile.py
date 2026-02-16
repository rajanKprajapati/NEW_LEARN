"""
Q2: Employee Payroll System

Abstract class Employee → abstract methods calculate_salary(), get_details()

Implement FullTimeEmployee and PartTimeEmployee

Print total payroll"""

from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    @abstractmethod
    def get_details(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self,Tsalary,bonus,pf,tex):
        self.Tsalary=Tsalary
        self.bonus=bonus
        self.pf=pf
        self.tex=tex

    def calculate_salary(self):
        total_earning=self.Tsalary+self.bonus
        total_reduction=self.pf+self.tex
        current_amount=total_earning-total_reduction
        return current_amount
    
    def get_details(self):
        print(f"Your Salary:{self.Tsalary},Bonus:{self.bonus},Pf:{self.pf},TEX:{self.tex}")
class PartTimeEmployee(Employee):
    def __init__(self,Tsalary,bonus):
        self.Tsalary=Tsalary
        self.bonus=bonus
    
    def calculate_salary(self):
        total_earning=self.Tsalary+self.bonus
        return total_earning

    def get_details(self):
        print(f"Your Salary:{self.Tsalary},Bonus:{self.bonus}")

    
nitesh=FullTimeEmployee(22000,2500,3700,2000)
print("Pay to Nitesh:",nitesh.calculate_salary())


    
