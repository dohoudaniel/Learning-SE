""" I wrote this code myself. """
#!/usr/bin/python3
def safe_print_division(a, b):
    """ A function that divides 2 integers and prints the result. """
    c = 0
    
    try:
        c = float(a // b)
    
    except (TypeError, ZeroDivisionError):
        c = None
        # return None
        
    finally:
        print("Inside result: {}".format(c))
        
    return c

