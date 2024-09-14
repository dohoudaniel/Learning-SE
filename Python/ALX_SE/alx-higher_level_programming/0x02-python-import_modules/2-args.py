#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and the list of arguments entered from the teminal"""
    import sys
    # For sys.argv, never forget to import sys
    
    dan =  len(sys.argv) - 1
    if dan == 0:
        print("0 arguments.")
    elif dan == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(dan))
    
    for i in range(dan):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
        
# The sys.argv[] function in Python gotten from importing sys works as the combination
# of the argc and argv functions in C.

