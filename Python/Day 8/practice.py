# Create online store for Products (name, price). Track the total order

class Products:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Products.count += 1

    def get_info(self):
        print(f'Price of {self.name} is {self.price}')

    @classmethod
    def get_count(cls):
        print(f'The total number of products is {cls.count}')

    @staticmethod
    def calc_discount(price, discount):
        print(f'Price after discount is {price-(price*discount/100)}')



p1 = Products("Laptop", 100_000)
p2 = Products("Smartphone", 50_000)
p3 = Products("Mouse", 1_000)
Products.get_count()
p1.calc_discount(p1.price, 15)

