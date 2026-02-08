# In multiple inheritance, super() helps Python follow the correct order (MRO = Method Resolution Order).


"""
Create class Account with balance and method deposit() and withdraw().
Create class SavingsAccount(Account) that adds interest_rate and method add_interest()."""

class Account:
    def __init__(self,balance):
        self.balance=balance

    def deposite(self,new_balance):
        self.balance+=new_balance 
        print("deposte successful")  

    def withdraw(self,cut_balance):
        self.balance-=cut_balance
        print("withdral successful")

class SavingsAccount(Account):
    def __init_(self,balance,interest_rate):
        super().__init__(balance)
        self.interest_rate=interest_rate

    def  add_interest(self,interest):
        self.balance+=interest
        print("interest added successfully")

#Example of the creating a Savingbank
obj=SavingsAccount(20000)
obj.add_interest(200)
print("Current balance is:")
print(obj.balance)
             
