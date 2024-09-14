#!/usr/bin/python3
"""
The filter function
"""

def even_numbers(x):
    """
    Returns true if x is an even number
    """
    if x % 2 == 0:
        return True
    else:
        return False

from return_square_root import square_root as squareRoot
my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81]
new_list = list(map(squareRoot, my_list))
print("new_list: ", new_list)
even_list = list(filter(even_numbers, new_list))
print("even_list: ", even_list)

