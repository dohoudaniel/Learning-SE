# Object Oriented Programming - Classes
# 0x06-python_classes

# Class And Object Variables
class Speedsters:
    """ Represent a Speedster with a name """

    # A class variable, that counts the number of speedsters
    number = 0

    # This is known as initializing function
    # The __init__ method is also known as the constructor method of the class
    def __init__(self, name):
        """ Initializing the data """
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, this speedster is added to the number of speedsters
        Speedsters.number += 1

    def speed_decrease(self):
        """ Speed of a speedster decreasing """
        print("{} is having a massive drain of the SpeedForce in him!".format(self.name))
        # When this happens, this speedster is removed from the number of speedsters
        Speedsters.number -= 1

        if Speedsters.number == 0:
            print("{} was and is the last speedster.".format(self.name))
        else:
            print("There are still {} running speedsters".format(Speedsters.number))

    def speech(self):
        """ Speech by the last speedster
            The Flash
        """
        print("I am the fastest man alive. I am {}".format(self.name))

    @classmethod
    # the '@classmethod' is a decorator
    def how_many(cls):
        """ Prints the current number of speedsters """
        print("There are {:d} speedsters.".format(cls.number))


# Reality - Instantiating the class
speedster1 = Speedsters("The Flash")    # self.name holds 'The Flash'
speedster1.speech()
Speedsters.how_many()

speedster2 = Speedsters("Kid Flash")
speedster2.speech()
Speedsters.how_many()

print("\nThe Race Begins...\n")

print("The race will soon end. Let's see how fast each of them goes...")
speedster2.speed_decrease()
speedster1.speed_decrease()

Speedsters.how_many()

# It seems that using the __init__ method actually initializes a variable that could be used as a class argument...


"""
Explanation
-----------
This is a long example but helps demonstrate the nature of class and object variables. Here, 'number' belongs to the 'Speedsters' class
and hence is a class variable. The 'name' variable belongs to the object (it is assigned using self) and hence is an object variable.

Thus, we refer to the 'number' class variable as 'Speedsters.number' and not as 'self.number'. We refer to the object variable name
using 'self.name' notation in the methods of that object. Remember this simple difference between class and object variables. Also note
that an object variable with the same name as a class variable will hide the class variable!
Also trying to access the 'name' through the class will result in an AttributeError since instance variables are object specific and are created when __init__ constructor is invoked. This is the central distinction between the class and instance variables.

Instead of 'Speedsters.number', we could have also used self.__class__.number because every object refers to its class via the self.__class__ attribute.

The how_many is actually a method that belongs to the class and not to the object. This means we can define it as either a classmethod or a staticmethod
depending on whether we need to know which class we are part of. Since we refer to a class variable, let's use classmethod.

We have marked the how_many method as a class method using a decorator ('@classmethod').

Decorators can be imagined to be a shortcut to calling a wrapper function (i.e. a function that "wraps" around another function so that it can do
something before or after the inner function), so applying the @classmethod decorator is the same as calling:
how_many = classmethod(how_many)

Observe that the __init__ method is used to initialize the 'Speedsters' instance with a name. In this method, we increase the number count by 1
since we have one more 'Speedsters' being added. Also observe that the values of self.name is specific to each object which indicates the nature
of object variables.

Remember, that you must refer to the variables and methods of the same object using the self only. This is called an attribute reference.

In this program, we also see the use of docstrings for classes as well as methods. We can access the class docstring at runtime using Speedsters.__doc__
and the method docstring as Speedsters.speech.__doc__

In the speed_decrease method, we simply decrease the 'Speedsters.number' count by 1.

All class members are public. One exception: If you use data members with names using the double underscore prefix such as __privatevar,
Python uses name-mangling to effectively make it a private variable.

Thus, the convention followed is that any variable that is to be used only within the class or object should begin with an
underscore and all other names are public and can be used by other classes/objects. Remember that this is only a convention
and is not enforced by Python (except for the double underscore prefix).
"""

