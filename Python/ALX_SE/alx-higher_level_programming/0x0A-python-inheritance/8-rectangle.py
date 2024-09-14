#!/usr/bin/python3
""" Implementing a Geometry class on a rectangle """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Implementing a rectangle
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        # Validating width and height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Concerning the integer_validator method, 
        # The name parameter represents the name of the attribute being validated ("width" or "height").
        # 'name' is a string when being outputted in the integer_validator method.
        # The value parameter represents the value of the attribute being validated (width or height).
