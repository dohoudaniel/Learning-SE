#!/usr/bin/python3
def safe_print_integer(value):
    """
    Arguments:
        value (int): The integer to print
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True
    """
    try:
        print("{:d}".format(value))
        return True
    
    except (TypeError, ValueError):
        return False
    
    # The return value from this file affects what the task1-main.py file will run.

