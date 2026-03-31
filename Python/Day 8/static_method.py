# Implement static method
# It doesn't need compulsory parameter

class Laptop:
    def __init__(self, name):
        self.name = name


    @staticmethod
    def calc_discount(price, discount):     # static method
        print(f'Price after discount is {price - (price*discount/100)}')


l1 = Laptop("Samsung")
l1.calc_discount(100000, 10)