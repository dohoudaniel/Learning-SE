#!/usr/bin/python3
"""Defines a JSON file-reading function."""


import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.
    Returns:
        An object created from a JSON file.
    """
    with open(filename) as f:
        # my_obj = json.load(f)
        # return my_obj
        return json.load(f)
