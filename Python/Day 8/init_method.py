# Program to implement init method

class Student:
    college_name = "rrlc"       # Class attribute
    def __init__(self, name, roll, cgpa):
        self.name = name        # Instance attribute
        self.roll = roll
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stud1 = Student("Rajnish", 10, 3.2)
stud2 = Student("Hari", 12, 3.0)
print(f"Student name: {stud1.name} \nStudent roll: {stud1.roll} \nCollge name: {stud1.college_name} ")
print(stud2.get_cgpa())