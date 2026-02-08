class ATM:
    def __init__(self,balance):
        self.__balance=balance
    
    #setter
    def deposite(self,Adding_balance):
        if Adding_balance>0:
            self.__balance+=Adding_balance  
            print(f"Your {Adding_balance} Rs has  deposite Succsessfully.")
    #grtter
    def withdraw(self,with_balance):
        if with_balance<=self.__balance:
            self.__balance-=with_balance
            print(f"{with_balance} Rs Withdrawed Succsessfully.")
    
    def check_balance(self):
        print(f"Current Balance is {self.__balance} Rs.")


user1=ATM(20000)
user1.deposite(2000)
user1.check_balance()
user1.withdraw(15000)
user1.check_balance()