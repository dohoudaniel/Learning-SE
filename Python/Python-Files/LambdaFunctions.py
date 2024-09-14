# import sys

""" The Lambda Operator """
# The lambda operator or the lambda function is a way to create small anonymous functions, i.e functions without a name.
# These functions are throw-away functions, i.e. they are just needed where they have been created.
# Lambda functions are mainly used in combination with the functions filter(), map() and reduce().
# The general syntax of a lambda function is:
#  Syntax:        lambda argument_list: expression
# The argument list consists of a comma separated list of arguments and
# The expression is an arithmetic expression using these arguments.
# You can assign the function to a variable to give it a name.

# The lambda function returns the sum of its two arguments:
Sum = lambda x, y: x + y
# print(Sum(4, 6))    # Output is 10

# This is the same as the lambda function
def Sum(x, y):
    return x + y;
# print(Sum(16, 84))



""" The map() function """
# The map() function takes in two arguments
# Syntax:    d = map(func, seq)
# The first argument, func, is the name of a function
# The second argument, seq, is the name of a sequence e.g a list
# map() applies the function func to all the elements of the sequence seq.
# With Python 3, map() returns an iterator.

# Example:
def Daniel(d):    # This function returns the square of the argument, i.e, the argument to the power of 2
    return d ** 2
song = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
square = map(Daniel, song)    # This returns the address of the map object in memory
# print(square)    # Output was: <map object at 0x0000023DEC0EBD90>

Square = list(map(Daniel, song))    # This returns a list of the values of song mapped to the function Daniel
# print(Square)    # Output is: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Note that in the example above, we did not use lambda. By using lambda, we wouldn't have had to define and name the function Daniel().
# This is how we use the lambda function:
Song = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Squares = list(map((lambda p : p ** 2), Song))
# print(Squares)

# map() can be applied to more than one list. he lists don't have to have the same length. map() will apply its lambda function to the
# elements of the argument lists, i.e. it first applies to the elements with the 0th index, then to the elements with the 1st index
# until the n-th index is reached:
past = [2, 4, 6, 8, 10, 12, 14]
fix = [10, 20, 20, 50, 50]
lists = list(map((lambda s, t: s + t), past, fix))
# It takes in two parameters in the lambda function here because there are two lists. 
# print(lists)
# When the lists passed as arguments are not of equal length, map() will stop when the shortest list is consumed.
present = [10, 20, 30, 40]
future = [100, 200, 300, 400, 500]
now = list(map((lambda P, F: P + F), present, future))
# print(now)    # Output is: [110, 220, 330, 440]


# Mapping a List of Functions
# We will write a function that applies a bunch of functions to one Python object
from math import sin, cos, tan, pi
def map_functions(m, funcs):
    """ map an iterable of functions on the object m """
    res = []
    for dan in funcs:
        res.append(dan(m))
    return res
family_of_functions = (sin, cos, tan)
# print(map_functions(pi, family_of_functions))




"""
Filtering  a list - The filter() function
"""
# Syntax -    filter(function, sequence)
# Example for explanation ->     filter(f, i)
# This function takes a function as its first argument. This function, f, must return a Boolean value, i.e either True of False.
# This function will be applied to every element of the list, i. Only if i returns True will the element be produced by the iterator,
# which is the return value of the filter() function.
# In the following example, we filter out first the odd and then the even elements of the sequence of the first 11 Fibonacci numbers:
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(sorted(filter(lambda x: x % 2 > 0, fibonacci)))    # Prints a sorted list.
# print(odd_numbers)    # This will happen only if x % 2 > 0 (an odd number), and filter() returns True.
even_numbers = list(sorted(filter(lambda x: x % 2 == 0, fibonacci)))    # Prints a sorted list
# print(even_numbers)   # This will occur only if x % 2 == 0 (an even number), and filter() returns True.
# As such, we can use the filter() function to filter out false values.



"""
Reducing a list - The reduce() function
"""
# Syntax:     reduce(func, seq)
# This function returns a single value.
# The reduce() function can be gotten from importing a higher-order function - functools
# Example:
import functools
# functools is a module in Python that provides functions for working with higher-order functions and callable objects.
# It is part of the standard library (sys). The functools module is for higher-order functions: functions that act on or return other functions.
# In general, any callable object can be treated as a function for the purposes of this module. Simple lightweight unbounded function cache.
# print(dir(functools))
reduce = functools.reduce(lambda x,y: x+y, [47,11,42,13])
print(reduce)
"""
What happened in the var reduce is
Since the function defined as the lambda takes in two arguments, and returns their addition, and we were given the list as [47,11,42,13]
What happened is:
return value of the lambda function is = ((47 + 11) + 42) + 13 = 113
"""
# The reduce() function is a method of the functools function, that is part of the standard library.
# That is why it is defined as:      functools.reduce()

