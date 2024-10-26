class Point:

    def __init__(self,x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    ### Overloading over sum operator --> +
    # Example: Sum 2 points, for example - (1,2) + (3,4) the result is new Point(4,6)
    ###
    def __add__(self,other):
       return Point(self.x + other.x,self.y + other.y)
    
    def __repr__(self) -> str:
        return f"Point: ({self.x},{self.y})"

    def __str__(self) -> str:
        return f"Point: ({self.x},{self.y})"

p1 = Point(1,2)
p2 = Point(3,4)

p3 = p1 + p2
print(p3)