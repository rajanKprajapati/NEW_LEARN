class User:
    def __init__(self,password):
        self.__password=password
    
    #setter 
    def setter(self,new_password):
        if len(str(new_password))>=6:
            self.__password=new_password
            print("Password has saved succsessfully")
        else:
            print("Invslide input")

    #getter
    def getter(self):
        return "Accessc Denied"
    
#  new object creation 
obj=User(4204221520047)
obj.setter(254563457)
print(obj.getter())
