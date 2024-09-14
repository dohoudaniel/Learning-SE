#!/usr/bin/python3

# import __future__
from __future__ import print_function
import sys

def safe_function(fct, *args):
    """
    A function that executes a function safely.
    fct will be always a pointer to a function
    The function returns the result of the function, that fct points to
    """
    
    # fct, a pointer to a function, will point to the function
    # The function, on being called here will take in the arguments and execute it along the functions.
    # *args is used to represent an arbitrary number of positional arguments
    
    # This block runs first to execute this file.
    try:
        dan = fct(*args)
    
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    
    else:
        return dan

