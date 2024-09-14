#!/usr/bin/python3
def magic_string():
    # The code below effectively keeps track of the number of times the magic_string() function 
    # has been called by storing it as an attribute of the function itself.
    magic_string.n = getattr(magic_string, 'n', 0) + 1

    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
