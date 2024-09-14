#!/usr/bin/python3

""" This function calculates the area of a circle. """
from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError("The value of the radius cannot be negative.")
    return (pi * (r**2))

"""
# Test Function since there is no docstring
radii = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of circles with radius r = {radius} is {area}."

for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))
"""
