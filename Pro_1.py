class item:
    def __init__(self):
        pass
    def hello(self,x,y):
        print( x*y)


item1=item()
item1.name="phone"
item1.price=100
item1.quintity=5
item1.hello(item1.price,item1.quintity)
print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quintity))
