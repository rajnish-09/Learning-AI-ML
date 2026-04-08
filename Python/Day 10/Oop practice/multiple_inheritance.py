# Create the following classes : Herbivore, Carnivore , Omnivore, with some attributes & methods.Then create a class that inherits from all the above classes to showcase how multiple inheritance works.

class Herbivore:
    def __init__(self, herbivore_food):
        self.herbivore_food = herbivore_food

class Carnivore:
    def __init__(self, carnivore_food):
        self.carnivore_food = carnivore_food

class Omnivore:
    def __init__(self, omnivore_food):
        self.omnivore_food = omnivore_food


class Person(Herbivore, Carnivore, Omnivore):
    def __init__(self, herbivore_food, carnivore_food, omnivore_food, name):
        Herbivore.__init__(self, herbivore_food)
        Carnivore.__init__(self, carnivore_food)
        Omnivore.__init__(self, omnivore_food)
        self.name = name

    def get_info(self):
        print(f'Name: {self.name} \nI eat {self.herbivore_food}, {self.carnivore_food}, {self.omnivore_food}')

p1 = Person("grass", 'meat', 'grass and meat', 'Ram')
p1.get_info()




