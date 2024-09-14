#!/usr/bin/python3
"""
Using the reduce function
"""
from functools import reduce
my_list = list(range(101))
# print(my_list)


def fibonacci(x, y):
    """
    Returns the addition of two arguments
    """
    return x + y


final_answer = reduce(fibonacci, my_list)
print(final_answer)
