# Implement class method
# cls is always the first parameter. This method can only access the class varibale. Can be accessed by Class name as well as object

class Student:
    college_name = 'rrlc'
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_college_name(cls):
        return cls.college_name
    
s1 = Student("Rajnish")
print(Student.get_college_name())
print(s1.get_college_name())