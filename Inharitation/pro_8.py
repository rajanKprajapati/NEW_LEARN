"""Create Company -> Manager -> TeamLead
Add attributes in each and print all."""
class Company:
    def __init__(self,company_name):
        self.company_name=company_name

class Manager(Company):
    def __init__(self,company_name,Manager):
        super().__init__(company_name)
        self.Manager=Manager

class Team_Lead(Manager):
    def __init__(self,company_name,Manager,team_lead):
        super().__init__(company_name,Manager)
        self.team_lead=team_lead

#creating an object
obj=Team_Lead("Tesla","Dilip Rastogi","Aditya Yadav")
#printing all the data
print("Compmey name:",obj.company_name)
print("Manager name:",obj.Manager)
print("Team Lead Name:",obj.team_lead)

