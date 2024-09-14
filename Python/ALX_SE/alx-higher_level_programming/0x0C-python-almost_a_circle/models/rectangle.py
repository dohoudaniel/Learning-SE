#!/usr/bin/python3
"""
Class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    Representing the Rectangle class
    Inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # The width getter function
    @property
    def width(self):
        """ Returning the private width attribte """
        return self.__width

    # The width setter function
    @width.setter
    def width(self, value):
        """ Validate the value for the width """
        # Validating if value is an int
        if type(value) is not int:
            raise TypeError("width must be an integer")
        
        # Validate if value <= 0
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value


    # The height setter function
    @property
    def height(self):
        """ Returning the private height attribute """
        return self.__height

    # The height setter function
    @height.setter
    def height(self, value):
        """ Validate the value for the height """
        # Validating if value is an int
        if type(value) is not int:
            raise TypeError("height must be an integer")

        # Validate if value <= 0
        if value <= 0:
            return ValueError("height must be > 0")

        self.__height = value


    # The x getter function
    @property
    def x(self):
        """ Returning the private x attribte """
        return self.__x

    # The x setter function
    @x.setter
    def x(self, value):
        """ Validate the value for x """
        # Validate if x is an integer
        if type(value) is not int:
            raise TypeError("x must be an integer")

        # Validate if x is greater than 0
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value


    # The y getter function
    @property
    def y(self):
        """ Returning the private y attribute """
        return self.__y

    # The y setter function
    @y.setter
    def y(self, value):
        """ Validate the value for y """
        # Validate if y is an integer
        if type(value) is not int:
            raise TypeError("y must be an integer")

        # Validate if y is greater than 0
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        area = self.width * self.height
        return area

    def display(self):
        """
        Prints to stdout the Rectangle instance
        with the character #
        """
        # Updating the function to handle for x and y
        # self.x handles the horizontal position of the rectangle
        # self.y handles the vertical position of the rectangle

        # Create an empty string
        rectangle = ""
        
        # Displaying the empty space for y
        print("\n" * self.y, end="")

        for i in range(self.height):
            # Printing the empty space in front of '#' for x
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"

        print(rectangle, end="")

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
                # setattr(self, key, value)
        else:
            # If args is not empty
            return
        """ Update arguments to an attrbute """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
            self.id, self.x, self.y, self.width, self.height))

    @staticmethod
    def setter_validation(attribute, value):
        """
        The setter_validation function
        This is the prototype of the method of validating instances
        of the class Rectangle that we used in the setter methods for
        width, height, x, and y
        """
        # Checking if value is an integer
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))

        # Checking if x or y is greater than 0
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def to_dictionary(self):
        """ Returns a dictionary representaion of our Rectangle instance.
        """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
