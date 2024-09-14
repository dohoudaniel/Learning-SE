#!/usr/bin/python3
def weight_average(my_list=[]):
    """ Returns the weighted average of all
    integers in a tuple (<score>, <weight>) 
    """
    if not my_list:
        return 0
    
    number = 0
    dan = 0
    
    for Dan in my_list:
        number = number + Dan[0] * Dan[1]
        dan = dan + Dan[1]
    
    return (number / dan)

