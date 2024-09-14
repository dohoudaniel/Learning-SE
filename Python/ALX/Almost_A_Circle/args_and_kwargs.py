#!/usr/bin/python3

# *args and **kwargs in Python explained
# Link: https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/

""" Example 1: """
def test_var_args(firstArg, *argv):
    print("first normal arg:", firstArg)
    for arg in argv:
        print("another arg through *argv :", arg)
# Calling the function
print("Calling the function using *args")
test_var_args("Daniel", "Dohou", "A Beautiful Mind")
print()


""" Example 2: """
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("{} == {}".format(key, value))
# Calling the function
print("Calling the function using **kwargs")
# greet_me(name="Barry Allen")
print()


""" Using *args and **kwargs to call a function """
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# Passing arguments to our function with *args
args = ("two", 5, "Hello.")
print("Calling a function with *args...")
test_args_kwargs(*args)

print()

# Passing arguments to our function with **kwargs
kwargs = {"arg1": "Daniel", "arg2":17, "arg3":"Programmer"}
print("Calling a function with **kwargs...")
test_args_kwargs(**kwargs)


