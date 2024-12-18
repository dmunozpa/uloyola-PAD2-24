from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self):
        self.area = None
        self.perimeter = None

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Figure):

    def __init__(self, width, height):
        super().__init__()
        self.height = height
        self.width = width

    def calculate_area(self):
        self.area = self.width * self.height

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: Height - ({self.height}) Width - ({self.width})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: Height - ({self.height}) Width - ({self.width})"


class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side,side)

    @property
    def side(self):
        return self.height

    def calculate_area(self):
        self.area = self.side * self.side

    def calculate_perimeter(self) -> None:
        self.perimeter = 4 * self.side

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} - Side: ({self.side})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} - Side: ({self.side})"


def main():

    # Example usage:
    newSquare = Square(10)
    newSquare.calculate_area()
    newSquare.calculate_perimeter()
    print(f"Square - Area: {newSquare.area}, Perimeter: {newSquare.perimeter}")

    print(newSquare)

    # Example usage:
    rectangle = Rectangle(5, 7)
    rectangle.calculate_area()
    rectangle.calculate_perimeter()
    print(f"Rectangle - Area: {rectangle.area}, Perimeter: {rectangle.perimeter}")

    print(rectangle)

if __name__ ==  "__main__":
    main()
