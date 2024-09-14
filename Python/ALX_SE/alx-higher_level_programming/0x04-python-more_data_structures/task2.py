#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ Adds all unique integers in a list (only once for each integer) """
    if not my_list:
        return None
    
    else:
        # sum = lambda x, y: x + y
        Sum = 0
        daniel = list(set(my_list))
        for p in daniel:
            Sum = Sum + p
        return Sum
        
        
        
"""
        for p in range(len(daniel)):
            while daniel[p] <= max(daniel):
                daniel[p] = daniel[p] + daniel[p+1]
                p = p + 1
                return p
"""
