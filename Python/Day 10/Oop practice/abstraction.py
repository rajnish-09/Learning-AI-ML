# Create abstract class Employee with abstract method calc_salary()
# Create subcass Intern, FullTimeEmployee, and ContractEmployee that implement the method differently

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calc_salary(self):
        pass


class Intern(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calc_salary(self):
        print(f"Intern salary: {self.salary} ")


class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calc_salary(self):
        print(f"Full time employee salary: {self.salary}")


class ContractEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calc_salary(self):
        print(f'Contract employee salary: {self.salary}')
    

i1 = Intern(10_000)
i1.calc_salary()

f1 = FullTimeEmployee(20_000)
f1.calc_salary()


c1 = ContractEmployee(25_000)
c1.calc_salary()