#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Representing a Square"""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square
        Args:
            size (int): The size of the new square
            position (int, int): The position of the new square
        """
        self.size = size
        self.position = position
        
    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)
        
    @size.setter
    def size(self, value):
        """Setting the values for value"""
        # size = self.__size
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """Get/Retrieve the current position of the square."""
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        """
        The code above (from after the method definition) can be written as:
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
        # Alternatively, it can be written as:
            # This uses a loop
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
        # Or:
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        """
        
    def area(self):
        """Returns the current area of the square."""
        area = self.__size ** 2
        return (area)
    
    def my_print(self):
        """Prints the square with the character '#' to stdout"""
        if self.__size == 0:
            print()
            return
        
        # position should be use by using space - Don’t fill lines by spaces when position[1] > 0
        for m in range(0, self.__position[1]):
            print("")
        
        # Looping through the value of 'size'
        for x in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")

