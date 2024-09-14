#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Representing a Square"""
    
    def __init__(self, size=0):
        """Initializing a new square
        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        """Returns the current area of the square."""
        area = self.__size ** 2
        return (area)

