#3️⃣ Multiple Inheritance
"""Create class Camera with method take_photo()
Create class Phone with method call()
Create class SmartPhone(Camera, Phone) and call both.(pro_11.py)
"""

class Camera:
    def take_photo(self):
        print("take a photo")

class  Phone  :
    def call(self):
        print("method that calls")

class SmartPhone(Camera,Phone):
    pass  

#calling both after creating the object
obj=SmartPhone()
obj.take_photo()
obj.call()
