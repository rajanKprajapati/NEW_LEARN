"""Create a class Employee with:

instance variables: name, salary

@classmethod from_string(data)
Input format: "Rajan-50000"
It should return an Employee object."""

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def from_string(cls,data):
        name,salary=data.split("-")
        return cls(name,int(salary))
    

# emp1=Employee("Rajan",100000)
# emp2=Employee("Nitesh",100500)
emp1=Employee.from_string("Rajan-100000")
emp2=Employee.from_string("Nitesh-100500")
name1,salary1=emp1
name2,salary2=emp2
print(name1,salary1)
print(name2,salary2)
