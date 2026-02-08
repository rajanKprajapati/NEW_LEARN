#without incaptulation
class Bank:
    def __init__(self,name,amount):
        self.name=name
        self.__amount=amount
    #getter
    def show(self):
        print(f"Your name is {self.name}\n Balence:{self.__amount}")

    #setter
    def set(self,amount):
        self.__amount=amount


costumer=Bank("Suman Prajapati",2153)
# print(costumer.name)
# print(costumer.amount)
print()
print("BEFORE UPDATE:") 
costumer.show()
costumer.set(100000)
print()
print("AFTER UPDATE:")
costumer.show()  
         