# Create base class Vehicle with attributes brand and model
# Create 2 subclass Car and Bike that add extra attribute seats (in car) and engine (in bike)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def get_info(self):
        print(f'Brand: {self.brand} \nModel: {self.model} \nSeats: {self.seats}')

    
class Bike(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine

    def get_info(self):
        print(f'\nBrand: {self.brand} \nModel: {self.model} \nEngine: {self.engine}')
    

c1 = Car("Toyota", "Hilux", 7)
c1.get_info()

b1 = Bike("Yamaha", "Ray zr", '125cc')
b1.get_info()