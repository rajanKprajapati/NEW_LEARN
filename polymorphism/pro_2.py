"""Create Employee class with calculate_salary()
Subclasses:

FullTimeEmployee

PartTimeEmployee

Freelancer
Each uses different logic"""

class Employee:
    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary()")

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary, bonus=0):
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Freelancer(Employee):
    def __init__(self, project_rate, projects_done):
        self.project_rate = project_rate
        self.projects_done = projects_done

    def calculate_salary(self):
        return self.project_rate * self.projects_done


employees = [
    FullTimeEmployee(50000, bonus=5000),
    PartTimeEmployee(500, 40),
    Freelancer(20000, 2)
]

for emp in employees:
    print(emp.calculate_salary())
emp.calculate_salary()
