class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print("Role:",self.role)
        print("Department:",self.department)
        print("Salary:",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT",60000)

e1=Employee("Manager","Finance",50000)
e1.showDetails()
eng1=Engineer("Rahul",25)
eng1.showDetails()