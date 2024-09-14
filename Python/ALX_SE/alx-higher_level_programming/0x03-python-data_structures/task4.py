#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return  my_list
    
    if idx > 0 and idx < (len(my_list) - 1):
        # Copy of my_list
        cat = [f for f in my_list]
        cat[idx] = element
        return cat

