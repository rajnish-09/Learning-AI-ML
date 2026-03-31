# Implement instance method
class Smartphone:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def get_brand(self):        # Instance method
        return self.brand
    
s1 = Smartphone("Apple", "Iphone 12", "Blue")
print(s1.get_brand())