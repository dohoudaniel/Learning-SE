#!/usr/bin/python3

# The reason for importing the sys module is stated below.
import sys

def safe_print_integer_err(value):
    """ A function that prints an integer.
    If a ValueError message is caught, a
    corresponding message will be printed
    to standard output.
    
    Arguments:
        value (int) - The integer to be printed
    Return:
        If a TypeError or ValueError occurs - False
        Otherwise - True 
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
    
# We imported the sys module (the standard header file for Python)
# because we need to get the error message returned during the execution
# of our file, and print it to standard output.
# The information during compilation is gotten from sys.exc_info()[1], and
# then it's involved with file=sys.stderr
# The file=sys.stderr is where the standard error is printed from.

