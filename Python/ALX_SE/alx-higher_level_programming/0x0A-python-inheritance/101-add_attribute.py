#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute will be added.
        attr_name: The name of the attribute to be added.
        attr_value: The value of the attribute to be added.
    Raises:
        TypeError: If the object already has an attribute with the given name.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
