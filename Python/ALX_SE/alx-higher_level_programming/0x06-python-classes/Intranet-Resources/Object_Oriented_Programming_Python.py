"""
Python - Object Oriented Programming
Link: https://python-course.eu/oop/object-oriented-programming.php
"""
x = 45
print(type(x))    # Output: <class 'int'>
pi = 3.142        # Output: <class 'float'>
print(type(pi))

def daniel(man):
    return man * man
print(type(daniel))    # Output: <class 'function'>

import math
print(type(math))    # Output: <class 'module'>



""" A Minimal Class In Python """
class Robot:
    pass
if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2)    # Returns True
    print(y == x)    # Returns False



""" Attributes """
class Robot:
    pass
x = Robot()
y = Robot()
x.name = "Marvin"
x.build_year = "1979"
y.name = "Caliban"
y.build_year = "1993"
print(x.name)
print(y.build_year)
# If you want to know, what's happening internally:
# The instances possess dictionaries __dict__, which they use to store their attributes and their corresponding values:
print(x.__dict__)
print(y.__dict__)

# Attributes can be bound to class names
class Robot(object):
    pass
x = Robot()
Robot.brand = "Kuka"
print(x.brand)    # Output: Kuka
x.brand = "Thales"    # This line is the reason for the ooutput on line 57
print(Robot.brand)    # Output: Kuka
y = Robot()
print(y.brand)    # Output: Kuka
Robot.brand = "Thales"
print(y.brand)    # Output: Thales
print(x.brand)    # Output: Thales
print(x.__dict__)    # Output: {'brand': 'Thales'}
print(y.__dict__)    # Output: {}
print(Robot.__dict__)    # Run for output
# print(x.energy)    # This returns an error

# By using the function getattr, you can prevent this exception, if you provide a default value as the third argument:
getattr(x, 'energy', 100)

# Binding attributes to objects is a general concept in Python. Even function names can be attributed.
# You can bind an attribute to a function name in the same way, we have done so far to other instances of classes:
def rf(x):
    return 42
rf.x = 40
print(rf.x)

# This can be used as a replacement for the static function variables of C and C++, which are not possible in Python.
# We use a counter attribute in the following example:
def ref(g):
    ref.counter = getattr(ref, "counter", 0) + 1
    return "Monty Python"
for i in range(10):
    ref(i)
    # print(ref.counter, end=' ')
# print()
print(ref.counter)



""" Methods """
# Let's define a function "hi", which takes an object "obj" as an argument and assumes that this object has an attribute "name".
# We will also define our basic Robot class again:
def hi(obj):
    print("Hi, I am " + obj.name + "!")
class Robot:
    pass
x = Robot()
x.name = "Marvin"
hi(x)
# We will now bind the function "hi" to a class attribute "say_hi"
def hi(obj):
        print("Hi, I am " + obj.name)
class Robot:
    say_hi = hi
x = Robot()
x.name = "Marvin"
Robot.say_hi(x)
# 'say_hi' is called a method. Usually, it will be called like this:
x.say_hi()


""" The __init__ method """
class A:
    def __init__(self):
        print("__init__ has been executed!")
dan = A()

