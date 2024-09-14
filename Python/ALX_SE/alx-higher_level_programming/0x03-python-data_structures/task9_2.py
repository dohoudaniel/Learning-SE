#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    # Using a for-loop to run through and search for the largest int
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]
    return (big)
# Understood

