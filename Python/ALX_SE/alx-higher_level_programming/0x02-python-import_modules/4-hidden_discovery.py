#!/usr/bin/python3

if __name__ == "__main__":
    """Print all the names defined by the hidden_4 module"""
    import hidden_4
    
    names = dir(hidden_4)
    """
        dir() - If called without an argument, return the names in the current scope.
        Else, return an alphabetized list of names comprising (some of) the attributes
        of the given object, and of attributes reachable from it.
    """
    
    for dan in names:
        if dan[:2] != "__":
            print(dan)

