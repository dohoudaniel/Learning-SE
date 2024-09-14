#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ A function that prints x elements of a list. """
    # x represents the number of elements to print
    # x can be bigger than the length of my_list
    
    d = 0
    
    try:
        # Runs through the x elements in the list
        for m in range(x):
            print(my_list[m], end='')
            d += 1

    except IndexError:
        None
    
    print()    # This prints a new line.

    # This returns the value of x.
    return d

