#!/usr/bin/python3
# 4-inherits_from.py

def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that
    inherited (directly or indirectly) from a specified
    class.
    Args:
        obj (any) : An object instance, the object to be checked.
        a_class : The specific class.
    Return:
        True - If the object is an instance of the specified class.
        False - If otherwise.
    """
    # return (type(obj) != a_class and isinstance(obj, a_class))
    # return (type(obj) is not a_class and isinstance(obj, a_class))
    return (type(obj) is not a_class and issubclass(type(obj), a_class))

"""
Explanation on functions used:
    type(obj) is not a_class == type(obj) != a_class
    - We use this function call to check that the type of the object is not exactly the same as the specified class (type(obj) is not a_class). This is to ensure that we are checking for inheritance and not a direct instance of the specified class.

    issubclass(type(obj), a_class) == isinstance(obj, a_class))
    - These function calls, here, are used to check if the type of the object or any of its parent classes (directly or indirectly) is a subclass of the specified class (a_class). This covers the condition of the object being an instance of a class that inherited from the specified class.
"""
