#!/usr/bin/python3
def multiply_by_2(a_dictionary):
   """ A function that returns a new dictionary with all values multiplied by 2 """
   daniel = {dan: (a_dictionary[dan] * 2) for dan in a_dictionary}
   return daniel

