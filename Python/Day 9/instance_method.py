# Create a class Student with attributes name and marks.
# Add a method grade() that prints “Pass” if marks ≥ 40 else “Fail”.
# Test with multiple students.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

stud1 = Student("Rajnish", 55)
stud1.grade()
stud2 = Student("Ramesh", 25)
stud2.grade()
