# Create a base class Employee with name and salary.
# Create a subclass Manager with extra attribute department.
# Add a method to display manager details including department.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def get_info(self):
        print(f"Name: {self.name} \nSalary: {self.salary} \nDepartment: {self.department}")

e1 = Manager("Ram", 20_000, "BCA")
e1.get_info()