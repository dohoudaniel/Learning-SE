#!/usr/bin/python3
# 2-is_same_class.py
""" Defines a class-checking function """


def is_same_class(obj, a_class):
    """ Checks if an object is exactly an instance of a specified class.
    Args:
        obj (any) : The object to check.
        a_class: The class to compare against.
    Returns:
        True - If obj is exactly an instance of a_class.
        False - Otherwise.
    """
    """
    if type(obj) == a_class:
        return True
    else:
        return False
    """
    return type(obj) is a_class
