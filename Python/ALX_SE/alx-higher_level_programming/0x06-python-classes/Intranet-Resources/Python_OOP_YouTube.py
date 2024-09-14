"""
Python: Object Oriented Programming
Link: https://www.youtube.com/watch?v=-DP1i2ZU9gk
"""
# Jehovahismyfather1234567

# Example 1 (x, y):
class Coordinate(object):
    # The parent of the class is the one that apperas in brackets after the class name (inheritance).
    # object is the very basic type in Python. It implements things like being able to assign variables
    """ A type called Coordinate. An object in Python """

    def __init__(self, x, y):
        # self is a placeholder for any form of instance when you create an object in a class
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return ( "<" + str(self.x) + ", " + str(self.y) + ">")

# Creating an instance of the object
c = Coordinate(3, 7)
# print(c.x, ",", c.y)
# print(c.distance(13))

print(c) # Output: <__main__.Coordinate object at 0x000001D76EDFFD50>
"""
What to do to modify a print statement:
define a __str__ method when used with 'print' on your class object.
You choose what it does!
"""
print(type(c))

# To confirm that we create a type in Python by creating a class
print(Coordinate)
print(type(Coordinate))


# A Fraction object
class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, " ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Returns a string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num * other.denom - self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)
    def __float__(self):
        """ Returns a float value of the fraction... """
        return self.num / self.denom
    def inverse(self):
        """ Returns a new fraction representing ... """
        return Fraction(self.denom, self.num)

# Instantiation - Initializing our class type  ( Added this comment by myself)
# Run for Output

a = Fraction(1, 4)
b = Fraction(3, 4)
c = a + b   # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))

