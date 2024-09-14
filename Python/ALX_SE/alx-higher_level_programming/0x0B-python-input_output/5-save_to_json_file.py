#!/usr/bin/python3
""" Saving an object to a file using JSON """


import json


def save_to_json_file(my_obj, filename):
    """ A function that writes an object to a text file
    using a JSON representation
    """
    with open(filename, "w") as f:
        # json_rep = json.dumps(my_obj)
        # f.write(json_rep)
        f.write(json.dumps(my_obj))
