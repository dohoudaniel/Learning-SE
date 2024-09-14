#!/usr/bin/python3
""" 3-is_kind_of_class.py """


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is exactly
    the instance of a specified calss.
    """
    if isinstance(obj, a_class) == True:
        return True
