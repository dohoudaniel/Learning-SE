#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ A function that deletes keys with a specific value in a dictionary. """
    
    # Making a list from the keys in the dictionary
    list_of_keys = list(a_dictionary.keys())
    
    # Iterating through the list_of_keys to delete the key and the value of the key
    # if the key == value (the argument)
    for value_dict in list_of_keys:
        if value == a_dictionary.get(value_dict):
            # The get() method is used to get the key and the value of a dictionary
            del a_dictionary[value_dict]
    
    return a_dictionary
    
    
    """y
    if value in a_dictionary:
        del a_dictionary[value]
    
    return a_dictionary
    """

