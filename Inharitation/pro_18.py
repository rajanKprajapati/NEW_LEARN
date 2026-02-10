"""Create parent Employee and child classes Developer, Designer, Tester
Each should override method work()."""


class Employee:
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        return "Developing a soft"

class Designer(Employee):
    def work(self):
        return "Designing a Program"

class Tester(Employee):
    def work(self):
        return "Testing a Developed app"

objs=[Developer(),Designer(),Tester()]
l=[i.work() for i in objs]
print(l)