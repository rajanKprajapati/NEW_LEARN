"""Create LoginSystem and PaymentSystem both have start() method.
Create EcommerceApp(LoginSystem, PaymentSystem)
Solve method conflict using:

super()

Explicit class calling (LoginSystem.start(self))"""

class LoginSystem:
    def start(self):
        print("now the Login is started")
        # super().start()

class PaymentSystem:
    def start(self):
        print("Now the payment is started")

class EcommerceApp(LoginSystem,PaymentSystem):
    def __init__(self):
        pass 
    def start(self):
        LoginSystem.start(self)      # explicit call
        PaymentSystem.start(self)    # explicit call

obj=EcommerceApp()
obj.start() #2.) Done
