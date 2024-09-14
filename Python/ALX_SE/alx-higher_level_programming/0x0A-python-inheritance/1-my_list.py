#!/usr/bin/python3
""" A class that inherits from 'list' """

class MyList(list):
    """ Inherits from list """

    def print_sorted(self):
        """ Returns a sorted list. """
        sorted_list = sorted(self)
        return sorted_list
