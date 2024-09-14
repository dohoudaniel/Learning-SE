#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevents the user from dynamically creating
    new LockedClass attributes for anything, but
    attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
    """
    The __slots__ attribute is a special attribute in Python that can be used to restrict
    the creation of instance attributes in a class. By setting __slots__ to 'first_name',
    we allow only the first_name attribute to be created for instances of the LockedClass.
    """
