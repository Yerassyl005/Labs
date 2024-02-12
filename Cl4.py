""" 
Write the definition of a Point class. Objects from this class should have a

* a method show to display the coordinates of the point
* a method move to change these coordinates
* a method dist that computes the distance between 2 points
"""
from math import sqrt

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point of coordinates: {self.x}, {self.y}")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def distance(self, second_point):
        return sqrt((self.x - second_point.x)**2 + (self.y - second_point.y)**2)
    
point1 = Point(5, 10)
point2 = Point(1, 7)

point1.display()
point2.display()

point1.move(10, 10)
point1.display()

print(f"The distance between two points is: {point1.distance(point2)}")
