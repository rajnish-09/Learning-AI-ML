# Create class Person that allows the constructor to work with name only, name + age, name + age + address

class Person:
    def __init__(self, name = None, age = None, address = None):
        if name is not None and age is not None and address is not None:
            print("Constructor with 3 parameters")
            self.name = name
            self.age = age
            self.address = address

        elif name is not None and age is not None:
            print("Constructor with 2 parameters")
            self.name = name
            self.age = age

        else:
            print("Constructor with a parameters")
            self.name = name


p1 = Person("Ram")
p2 = Person("Hari", 22)
p3 = Person("Shyam", 25, "Ktm")

print(p1.name)
print(p2.name, p2.age)
print(p3.name, p3.age, p3.address)

            