#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class  MyInt(int):
    """
    A class that inherits from the 'int' class.
    This class inverts int operators  == and !=.
    """

    def __eq__(self, intValue):
        """ The equal-to magic method.
        Override == opeartor with the != operator.
        """
        # The self.real attribute represents the actual integer value of the MyInt object.
        return self.real != intValue

    def __ne__(self, intValue):
        """ The not-equal-to magic method.
        Override the != operator with the operator.
        """
        # The self.real attribute represents the actual integer value of the MyInt object.
        return self.real == intValue
