#!/usr/bin/python3

""" A function that returns a list of available attributes and methods of an object """
def lookup(obj):
    attributes = []
    methods = []

    # Iterate over all attributes of the object
    for attr in dir(obj):
        # Exclude built-in attributes and methods
        if not attr.startswith('__'):
            value = getattr(obj, attr)
            # Check if it is a method or attribute
            if callable(value):
                methods.append(attr)
            else:
                attributes.append(attr)

    # Combine attributes and methods into a single list
    result = attributes + methods
    return result
