# Create a class Item that keeps track of total items created using a class variable.
# Create 5 objects and print the total count.

class Item:
    counter = 0

    def __init__(self, name):
        self.name = name
        Item.counter += 1
    
i1 = Item("Fridge")
i2 = Item("TV")
i3 = Item("Laptop")
i4 = Item("Speaker")

print(Item.counter)