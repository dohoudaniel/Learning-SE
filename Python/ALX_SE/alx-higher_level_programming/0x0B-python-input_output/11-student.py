#!/usr/bin/python3
"""
Module: student
Defines the Student class
"""


class Student:
    """
    Class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): A list of attribute names to be retrieved (default: None).
                If provided, only the attributes in the list will be included in the dictionary.
                If None, all attributes will be included.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values from the provided dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs.

        Note:
            This method assumes that the dictionary keys match the public attribute names of the Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
