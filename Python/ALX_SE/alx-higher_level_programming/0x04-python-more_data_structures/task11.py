#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """ A function that returns a list with all values multiplied by a number without using any loops. """
    Daniel = list(map(lambda daniel: daniel * number, my_list))
    return Daniel

