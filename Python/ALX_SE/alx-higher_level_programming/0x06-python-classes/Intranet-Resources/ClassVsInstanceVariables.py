# Class VS Instance Variables - Medium
# Link: https://medium.com/python-features/class-vs-instance-variables-8d452e9abcbd

class Car:
    wheels = 4    # A Class Variable

    # The initializing function
    def __init__(self, name):
        self.name = name    # Instance Variable

# Reality - Instantiating the class
jag = Car('Jaguar')
fer = Car('Ferrari')
print(jag.name)
print(fer.name)
print(jag.wheels)
print(fer.wheels)
# print(jag.wheels, fer.wheels)


"""
Trying to access the 'name' through the class will result in an AttributeError since
instance variables are object specific and are created when __init__ constructor
is invoked. This is the central distinction between the class and instance variables.
"""
print(Car.wheels)    # This works
# print(Car.name)    # Output: AttributeError: type object 'Car' has no attribute 'name' . This does not work.


# Modifying a class variable from the class
Car.wheels = 3    # We modified the 'wheels' variable.
print("{}, {}".format(jag.wheels, fer.wheels))
"""
Therefore modifying a class variable on the class namespace affects all the instances of the class.
"""

# Modifying a class variable for an instanceobject of the class itself, from the instance
Car.wheels = 4
print(jag.wheels)
print(fer.wheels)
jag.wheels = 3    # This creates a new instance variable with the same name as the class variable, 'wheels'.
print(jag.wheels)
print(fer.wheels)
"""
We modified the 'wheels' variable for jag.
Although we got the result we wanted, but what happened behind the scenes is a new 'wheels' variable that has been
added to 'jag' object and this new variable shadows the class variable with same name, overriding and hiding it.
We can access both the wheels variable as below.
"""
print("The value for \'jag.wheels\' is {}, and the value for \'jag.__class__.wheels\' is {}."\
      .format(jag.wheels, jag.__class__.wheels))
# jag.wheels -> The new instance variable with the same name as the class variable.
# jag.__class__.wheels -> The class variable itself.

"""
- Class variables are shared across all objects while instance variables are for data unique to each instance.
- Instance variable overrides the Class variables having same name which can accidentally introduce bugs or surprising behaviour in our code.
"""

