import math
# We will nedd to import math library.
# Create the abstract class Figure
class Figure:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

# Square class
class Square(Figure):
    def __init__(self, side=1):
        super().__init__()
        # TODO: Set the attribute: side

    def calculate_area(self):
        # TODO: Calculate the area: area = side*side 
        pass

    def calculate_perimeter(self):
        # TODO: Calculate the perimeter: perimeter = 4 * side
        pass

#  Circle class
class Circle(Figure):
    def __init__(self, radius=1):
        super().__init__()
        # TODO: Set the attribute: rasius


    def calculate_area(self):
        # TODO: Calculate the area = math.pi * radius^2
        pass

    def calculate_perimeter(self):
        # TODO: Calculate the perimeter = 2* math.pi * radius
        pass 

# Triangle class 
class Triangle(Figure):
    def __init__(self, side=1):
        super().__init__()
        # TODO: Update the atritutes

    def calculate_area(self):
        # TODO: First calctulate the height = ( sqrtr 3 / 2 ) * side
        # TODO: update the area = (side*height) / 2
        pass

    def calculate_perimeter(self):
        # TODO: Set the perimeter ? 3 * side.
        pass
        
# rectangle class
class Rectangle(Figure):
    def __init__(self, height=1, width=1):
        super().__init__()
        #TODO Update the atritutes

    def calculate_area(self):
        # TODO: Set the Area = leght * with
        pass

    def calculate_perimeter(self):
        # TODO: Set the perimeter = 2 * ( legnth + with)
        pass

if __name__ == "__main__":
    square = Square(5)
    square.calculate_area()
    square.calculate_perimeter()
    print("Square Area:", square.area)
    print("Square Perimeter:", square.perimeter)

    circle = Circle(3)
    circle.calculate_area()
    circle.calculate_perimeter()
    print("Circle Area:", circle.area)
    print("Circle Perimeter:", circle.perimeter)

    triangle = Triangle(4)
    triangle.calculate_area()
    triangle.calculate_perimeter()
    print("Triangle Area:", triangle.area)
    print("Triangle Perimeter:", triangle.perimeter)

    rectangle = Rectangle(6, 8)
    rectangle.calculate_area()
    rectangle.calculate_perimeter()
    print("Rectangle Area:", rectangle.area)
    print("Rectangle Perimeter:", rectangle.perimeter)

