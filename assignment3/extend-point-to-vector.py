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

# Create a couple of trucks
truck1 = Point(10, 5)
truck2 = Point(1, 1)
truck3 = Point(10, 5)

print(truck1 == truck2)
print(truck1 == truck3)
print(truck1)
print(truck1.distance(truck2))