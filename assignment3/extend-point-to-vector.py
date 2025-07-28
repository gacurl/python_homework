# Task 5: Extending a Class
import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance(self, other): # d = √((x2 - x1)² + (y2 - y1)²)
        return f"The distance between the two points is {round(math.sqrt(pow((self.x - other.x), 2) + pow((self.y - other.y), 2)), 3)}"

class Vector(Point): # inherits from Point
    def __init__(self, x, y):
        # Call the parent class's __init__ to set x/y
        super().__init__(x, y)

    def __str__(self):
        return f"<{self.x}, {self.y}>"
    
    def __add__(self, other):
        return f"The new vector is <{self.x + other.x}, {self.y + other.y}>"

# Create a couple of trucks
truck1 = Point(10, 5)
truck2 = Point(1, 1)
truck3 = Point(10, 5)
plane1 = Vector(10, 5)
plane2 = Vector(5, 10)

print(truck1 == truck2)
print(truck1 == truck3)
print(truck1)
print(truck1.distance(truck2))

print(f"Plane is at {plane1}")
print(plane1 + plane2)