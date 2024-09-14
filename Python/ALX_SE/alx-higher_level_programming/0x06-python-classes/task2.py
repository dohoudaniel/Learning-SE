#!/usr/bin/python3
"""A Class Square"""


class Square:
    """Represents a Square"""
    
    def __init__(self, size=0):
        """Initializing a square
        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

