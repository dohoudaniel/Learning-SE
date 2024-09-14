#!/usr/bin/python3
# Learning about the lambda, filter, reduce and map
# Link: https://python-course.eu/advanced-python/lambda-filter-reduce-map.php
"""
The map() functions
"""
from return_square_root import square_root as squareRoot


def square(iterable):
    """
    Finds the square of a number
    """
    return iterable ** 2


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# square_list = map(square, my_list) --- <map object at 0x00000275E8327010>
square_list = list(map(square, my_list))
print("Square List: ", square_list)

square_root_list = list(map(squareRoot, square_list))
print("Square Root List: ", square_root_list)
