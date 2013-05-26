# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = float(base)
        self.height = float(height)

    def area(self):
        """Returns area of the triangle"""
        return (0.5 * self.base * self.height)

    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)

    def __eq__(self,other):
        """Two triangle are equal if they have the same base
            and the same height"""
        return (self.base == other.base) and (self.height == other.height)
       

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet(object):
    
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.noOfShapes = 0
        self.parameters = {}
        self.pos = None
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """

##        if type(sh) == Triangle:
##            p = (sh.base,sh.height)
##
##        if type(sh) == Circle:
##            p = (sh.radius)
##
##        if type(sh) == Square:
##            p = (sh.side)

        self.parameters[self.noOfShapes]=sh
        self.noOfShapes += 1

        
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.pos = 0
        return self

    def next(self):
        if self.pos >= len(self.parameters):
            raise StopIteration

        self.pos += 1
        return self.parameters[self.pos - 1]
        
    
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        for p in self:
            print p
        return ''

##Debugging Code
##
##t = Triangle(3,4)
##s = Square(5)
##c = Circle(7)
##sets = ShapeSet()
##sets.addShape(t)
##sets.addShape(s)
##sets.addShape(c)
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largest = ()
    listOfAreas = []

    for e in shapes:
        listOfAreas.append(e.area())

    maximumArea = max(listOfAreas)

    for e in shapes:
        if e.area() == maximumArea:
            largest += (e,)

    return largest

##Debugging code
##
##t = Triangle(3,4)
##s = Square(5)
##c = Circle(7)
##t2 = Triangle(5,10)
##sets = ShapeSet()
##sets.addShape(t)
##sets.addShape(s)
##sets.addShape(c)
##sets.addShape(t2)
##large = findLargest(sets)
##print large
##for e in large: print e

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    

