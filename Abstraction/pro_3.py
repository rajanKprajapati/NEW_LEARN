"""Q3: Bank Account System
Abstract class BankAccount → abstract methods deposit(amount), withdraw(amount)
Implement SavingsAccount (min balance) and CurrentAccount (overdraft)
Function to transfer money
"""

from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass

class SavingAccount(BankAccount):
    def __init__(self,name,min_balance):
        self.name=name
        self.min_balance=min_balance

    def withdraw(self, amount=0):
        if amount>0:
            if amount<=(self.min_balance-5000):
                self.min_balance-=amount 
                return f"{amount} Rs has withdrawed sucsessfully"
            else:
                return f"The bank account is not allow This amount {amount} Rs"
        else:
            print("Amount is not valid")    
        
    def deposit(self,amount=0):
        self.min_balance+=amount
        return f"{amount} Rs has deposited sucssesfully"
    

class CurrentAccoun(BankAccount):
    def __init__(self,name,overdraft):
        self.name=name
        self.balance=overdraft

    def withdraw(self, amount=0):
        if amount>0:
            if amount<=(self.balance+10000):
                self.overdraft-=amount 
                return f"{amount} Rs has withdrawed sucsessfully"
            else:
                return f"The bank Account is not allow This amount {amount} Rs"
            
        else:
            print("Amount is not valid")    
        
    def deposit(self,amount=0):
        self.overdraft+=amount
        return f"{amount} Rs ha deposited sucssesfully" 


Cos1=SavingAccount("Bhola",20000)
Cos2=SavingAccount("Vimal",33000)
print(Cos1.withdraw(1000))
print(Cos1.deposit(2000))
print(Cos2.withdraw(10000))
print(Cos2.deposit(20300))

       
          

