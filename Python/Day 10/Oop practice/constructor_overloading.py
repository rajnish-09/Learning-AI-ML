class Person:
    def __init__(self, name=None, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

        if name and age and address:
            print("Constructor with 3 parameters")
        elif name and age:
            print("Constructor with 2 parameters")
        elif name:
            print("Constructor with 1 parameter")
        else:
            print("Default constructor")


p1 = Person("Ram")
p2 = Person("Hari", 22)
p3 = Person("Shyam", 25, "Ktm")

print(p1.name, p1.age, p1.address)
print(p2.name, p2.age, p2.address)
print(p3.name, p3.age, p3.address)