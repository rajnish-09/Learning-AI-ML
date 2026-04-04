# Create classes Dog and Cat, each with a method speak().
# Create a list of animals [Dog(), Cat(), Dog()] and call speak() for each to demonstrate polymorphism.

class Dog:
    def speak(self):
        print("Dog barks.")

class Cat:
    def speak(self):
        print("Cat meows.")

animals = [Dog(), Cat()]
for each in animals:
    each.speak()