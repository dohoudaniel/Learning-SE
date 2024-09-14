#!/usr/bin/python3
def best_score(a_dictionary):
    """ Return a key with the largest value """
    if not a_dictionary:
        return None
    
    return max(a_dictionary.keys())
    # return max(a_dictionary, key=a_dictionary.get)
    # return max(a_dictionary.values())

    """
    There are two methods that can be used for dictionaries:
    .keys()      and
    .values()
    """

