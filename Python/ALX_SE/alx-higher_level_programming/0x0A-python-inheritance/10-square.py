#!/usr/bin/python3
""" Implementing a square """


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    def __init__(self, size):
        """
        Initialize a new square.
        Args:
            size (int) : The size of the new square.
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        square = self.__size ** 2
        return square

    """
    def __str__(self):
        return super().__str__()
    """
