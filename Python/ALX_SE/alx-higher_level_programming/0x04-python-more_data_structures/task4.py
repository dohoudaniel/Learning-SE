#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ Returns the set of all elements present in only one set."""
    # This returns all the elements in both sets, but not the elements that are common within the two sets.
    daniel = set_1 ^ set_2
    return (daniel)

