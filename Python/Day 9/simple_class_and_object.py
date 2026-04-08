# Create a class Person with attributes name and age.
# Add a method display() to print the details.
# Create 2 objects and call the method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"Name: {self.name} \nAge: {self.age}")


p1 = Person("Rajnish", 20)
p1.get_info()
p2 = Person("Sumindra", 22)
p2.get_info()