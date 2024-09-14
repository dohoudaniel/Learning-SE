#!/usr/bin/python3
""" 2-is_same_class.py """


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly
    the instance of a specified calss.
    """
    if isinstance(obj, a_class) == True:
        return True
