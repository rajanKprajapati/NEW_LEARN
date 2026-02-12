"""Create Payment class with pay() method:

pay(amount)

pay(amount, method)

pay(amount, method, discount) """

class Payment:
    def pay(self,*data):
        if len(data)==1:
            print("amount",data[0])
        elif len(data)==2:
            print("amount",data[0])
            print("Mthod of payment:",data[1])
        else:
            print("amount",data[0])
            print("Mthod of payment:",data[1])
            print("Discount:",data[2])

obj=Payment()
obj.pay(200)  
print()
obj.pay(2000,"Phonepay")
print()
obj.pay(20000,"GPay","20%")         


