
# importing methods from different libraries needed to perform the calculations 
import math
import Shapes 

# below is all of the 3d shapes represented by classes. Each class contains methods for area and volume
# with the specific class attributes passed through them 

class Cuboid:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def area(self):
        return 2 * ((self.width * self.depth) + (self.height * self.depth) + (self.height * self.width))

    def volume(self):
        return self.width * self.height * self.depth


class Cube(Cuboid):
    def __init__(self, sideLength ):
        super().__init__(sideLength, sideLength, sideLength)


class Cylinder:
    def __init__(self, radius, height):
        self.height = height
        self.radius = radius
        self.base = Shapes.Circle(radius).GetArea()
    
    def area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * self.base)
    
    def volume(self):
        return self.base * self.height


class Sphere:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 4 * math.pi * (self.radius ** 2)
    
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)


class Prism:
    def __init__ (self, sideLength, sides, height):
        self.base = Shapes.Polygon(sideLength, sides).GetArea()
        self.perimeter = Shapes.Polygon(sideLength, sides).GetPerimeter()
        self.height = height

    def area(self):
        return (2 * self.base) + (self.perimeter * self.height)
    
    def volume(self):
        return self.base * self.height 
