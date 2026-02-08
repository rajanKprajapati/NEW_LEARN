"""Create a class User with @staticmethod is_valid_password(password)
Condition:

password length must be >= 8
Return True/False."""

class User:
    @staticmethod
    def is_valide_password(password):
        if len(str(password)) >=8: #convering all data type in string
            return "valid password"
        
obj1=User()
print(User.is_valide_password(124409703755495))
print(obj1.is_valide_password("@#&6306149&#@"))        