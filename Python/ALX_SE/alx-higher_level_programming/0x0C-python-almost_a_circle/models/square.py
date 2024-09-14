#!/usr/bin/python3

""" Square.py """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Representation of a Square based on the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiating method / constructor
        Note:
            Square.size = Rectangle.width
            Square.size = Rectangle.height
            Square.x = Rectangle.x
            Square.y = Rectangle.y
            Square.id = Rectangle.id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Return the size of the square """
        # It returns self.width because width is tefirst argument of its instance
        return self.width

    @size.setter
    def size(self, value):
        """ Validating the setter for the size of the square """
        self.width = value
        self.height = value

    def __str__(self):
        """ The string representation of Square """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id,
                                              self.x,
                                              self.y,
                                              self.width))

    def update(self, *args, **kwargs):
        """ Assigning attributes """
        # Checking if args is empty
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of Square
        """
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
