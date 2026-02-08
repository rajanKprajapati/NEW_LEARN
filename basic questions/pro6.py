class Balance:
    def __init__(self,amount):
        self.amount=amount

    def diposit(self,dipo):
        self.amount+=dipo
        print("Diposit amount:",dipo,"\nThankyou")

    def withdraw(self,get):
        self.amount-=get 

    def get_balance(self):
        print("Current Balance:",self.amount)       

account1=Balance(10000) 
account1.diposit(20000)      
account1.get_balance()
account1.withdraw(5965)
account1.get_balance()