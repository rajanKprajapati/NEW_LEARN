class Book:
    def __init__(self,tittle,price):
        self.__tittle=tittle
        self.__price=price

    #setter for price
    def price_setter(self,new_price):
        if new_price>0:
            self.__price=new_price
            print("\nNew Price has setted.")

    #getter for price
    def price_getter(self):
        print(f"\nBook Price: {self.__price} Rs") 

    #getter for tittle
    def tittle_getter(self):
        print(f"\nBook Tittle: {self.__tittle}") 

    #display
    def display(self):
        print(f"\nBook Tittle: {self.__tittle}\nBook Price: {self.__price}")     

user1=Book("Hand's On Machine Learning",1599)
user1.price_getter()
user1.tittle_getter()
user1.price_setter(3499)
user1.price_getter()
user1.tittle_getter()
user1.display()
