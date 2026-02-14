"""Question:
Create Vector3D class (x, y, z). Overload:
+ → add vectors component-wise
* → dot product of two vectors
== → compare if magnitudes are equal
str() → print nicely"""

import math
class Vector3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        return Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)
    
    def __mul__(self,other):
        return (self.x*other.x,self.y*other.y,self.z*other.z)
    
        
    def __eq__(self, other):
            return self.magnitude()== other.magnitude()
        
    def magnitude(self):
        return math.sqrt((self.x**2+self.y**2+self.z**2))
    
    def __str__(self):
        return f"x:{self.x},y:{self.y},z:{self.z}"
    
v1=Vector3D(1,2,3)
v2=Vector3D(3,2,1)
v3=v1+v2
print("New object rith the combination of the v1 and v2:")
print(v3)
print("Multiplication of the v1 & v2")
print(v1*v2)
print("Equility check:")
print(v1==v2)     
