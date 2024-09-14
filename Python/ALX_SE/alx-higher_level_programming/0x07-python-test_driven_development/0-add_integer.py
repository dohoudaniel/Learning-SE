#!/usr/bin/python3
"""Defines an integer-addition function."""

def add_integer(a, b=98):
    """
    Adds two integers a and b and returns the result.

    Args:
        a: An integer or float.
        b: An integer or float.

    Returns:
        An integer, the sum of a and b.

    Float arguments are typecasted to integers before addition is performed.
    
    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    # Checking if a is an integer or a float
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    # Checking if b is an integer or a float
    if ((inot isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    # The return statement - where the calculation is done.
    return (int(a) + int(b))
