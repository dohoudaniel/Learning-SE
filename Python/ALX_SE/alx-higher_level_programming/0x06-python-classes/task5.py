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
    
    def my_print(self):
        """Prints the square with the character '#' to stdout"""
        for d in range(0, self.__size):
            for m in range(self.__size):
                print("#", end="")
            print()
        
        if self.__size == 0:
            print()

