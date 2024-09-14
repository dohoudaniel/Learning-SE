#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Representing a Square"""
    
    def __init__(self, size=0):
        """Initializing a new square
        Args:
            size (int): The size of the new square
        """
        self.size = size
        
    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size
        
    @size.setter
    def size(self, value):
        """Setting the values for value"""
        # size = self.__size
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Returns the current area of the square."""
        area = self.__size ** 2
        return (area)
    
    def __eq__(self, other):
        """
        Define the == comparision to a Square. Returns a Boolean Value
        
        The __eq__ operator in Python is a method for overloading the
        default == operator, i.e. to define if two objects are equal.
        It returns True if the objects are equal, and False if otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Define the != comparison to a Square. Returns a Boolean Value
        
        The __ne__ operator in Python is a method for overloading the
        default != operator, i.e to define if two objects are not equal.
        It returns True if the objects are not equal, and False if otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()

