# Create a cass Shape with method area
# Create subcass Circle, Rectange, Triangle that overrride area method

class Shape:
    def area(self):
        pass


class Circe(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius
    

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 1/2 * self.base * self.height
    

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
c1 = Circe(5)
print(f"Area of circle: {c1.area()}")

t1 = Triangle(4,3)
print(f'Area of trianlge is: {t1.area()}')

r1 = Rectangle(7,4)
print(f'Area of rectangle is: {r1.area()}')