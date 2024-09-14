#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Finds all the multiples of 2 in a list
    multiple = []
    
    for m in range(len(my_list)):
        # if i is a multiple of 2
        if my_list[m] % 2 == 0:
            multiple.append(True)
        else:
            multiple.append(False)
        
    return multiple

