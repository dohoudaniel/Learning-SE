#!/usr/bin/python3

"""
Using args and kwargs in Python
Link: https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3
"""

def mult(x, y):
    print (x * y)

mult(5, 4)
print()


# Using *args to accept variable arguments
def flexible_multiply(*args):
    z = 1
    for num in args:
        z = z * num
    print(z)
flexible_multiply(4, 5)
flexible_multiply(10, 9)
flexible_multiply(2, 3, 4)
flexible_multiply(3, 5, 10, 6)
print()



# Using **kwargs
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
print()


# Using **kwargs for dictionary
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
print_values(my_name="Sammy", your_name="Casey")    # Dictionaries are unordered
print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )
print()


# Ordering arguments using args and kwargs
# Syntax:
    # def example(arg_1, arg_2, *args, **kwargs):


# Using args and kwargs in function calls
# 1. Tuples
def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)
args = ("Sammy", "Casey", "Alex")    # A tuple
some_args(*args)
print()

# 2. Lists
def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)
my_list = [2, 3, ]
some_args(1, *my_list)
print()

# 3. Dictionaries
def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)
my_kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
some_kwargs(**my_kwargs)
print()

