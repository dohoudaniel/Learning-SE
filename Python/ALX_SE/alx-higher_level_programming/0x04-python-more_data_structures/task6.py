#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ A function that prints a dictionary by ordered keys. """
    if not a_dictionary:
        return None
    
    # Keys should be sorted in alphabetic order
    # For dictionaries, there is a method - .keys() to access the keys.
    for daniel in sorted(a_dictionary.keys()):
        print("{}: {}".format(daniel, a_dictionary[daniel]))

