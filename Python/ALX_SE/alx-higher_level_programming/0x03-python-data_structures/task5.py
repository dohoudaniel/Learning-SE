#!/usr/bin/python3
def no_c(my_string):
    """ Removes all c and C characters from a string """
    daniel = "" # An empty string to store the new string without 'c' and 'C'
    
    for f in range(len(my_string)):
        if my_string[f] != 'c' and my_string[f] != 'C':
            daniel = daniel + my_string[f]
    
    return daniel

