#!/usr/bin/python3
""" A function that returns the 
    JSON representation of a string.
"""


import json


def to_json_string(my_obj):
    """ Convert my_obj to a JSON String representation
    Returns:
        JSON string representation of my_obj
    """
    # json_value = json.dumps(my_obj)
    # return json_value
    return json.dumps(my_obj)
