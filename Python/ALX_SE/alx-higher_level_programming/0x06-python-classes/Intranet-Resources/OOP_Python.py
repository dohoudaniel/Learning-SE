"""
Python - Object Oriented Programming
Link: https://python-course.eu/oop/object-oriented-programming.php
"""
""" Data Abstraction, Data Encapsulation, and Information Hiding """
# Encapsulation is seen as the bundling of data with the methods that operate on that data.

""" Data Abstraction = Data Encapsulation + Data Hiding """

# Encapsulation is often accomplished by providing two kinds of methods for attributes:
# - The methods for retrieving or accessing the values of attributes are called getter methods.
# Getter methods do not change the values of attributes, they just return the values.
# - The methods used for changing the values of attributes are called setter methods.

class Robot:
    def __init__(self, name=None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
x = Robot()
x.set_name("Henry")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())

# Exercise:
class Robot:
    def __init__(self,
                 name=None,
                 build_year=None):
        self.name = name
        self.build_year = build_year
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_build_year(self, by):
        self.build_year = by
    def get_build_year(self):
        return self.build_year
x = Robot("Henry", 2008)
y = Robot()
y.set_name("Marvin")
x.say_hi()
y.say_hi()


""" The __str__ and __repr__ methods """
# __str__ - The str() function

# Lists
dm = ["Python", "Java", "C++", "Perl"]
print(dm)    # dm is a list
str(dm)  # This should be run in the Python interpreter. This converts dm from a list to a string.
repr(dm)   # This should be run in the Python interpreter. This also converts dm from a list to a string.

# Dictionaries
d = {"a":3497, "b":8011, "c":8300}
print(d)
str(d)    # "" This should be run in the Python interpreter. This converts dm from a dictionary to a string. """
repr(d)    # This should be run in the Python interpreter. This converts dm from a dictionary to a string.

# Floats
fm = 306.172
print(fm)
str(fm)    # This should be run in the Python interpreter. This converts dm from a float to a string.
repr(fm)    # This should be run in the Python interpreter. This converts dm from a float to a string.

"""
If you apply str or repr to an object, Python is looking for a corresponding method __str__ or __repr__ in the class definition of the object.
If the method does exist, it will be called. In the following example, we define a class A, having neither a __str__ nor a __repr__ method.
We want to see, what happens, if we use print directly on an instance of this class, or if we apply str or repr to this instance:
"""
class A:
    pass
a = A()
print(a)    # Output: <__main__.A object at 0x0000029109AB3250>
print(repr(a)) # Output: <__main__.A object at 0x0000020EFFAE7190>
print(str(a)) # Output: <__main__.A object at 0x00000192F33A7190>
print(a) # Output: <__main__.A object at 0x0000024403A67190>

"""
If a class has a __str__ method, the method will be used for an instance x of that class, if either the function str is applied to it or if it
is used in a print function. __str__ will not be used, if repr is called, or if we try to output the value directly in an interactive Python shell:
"""
class A:
    def __str__(self):
        return "42"
a = A()
print(repr(a))    # Output: <__main__.A object at 0x000002B819467690>
print(str(a))    # Output: 42
print(a)

"""
Otherwise, if a class has only the __repr__ method and no __str__ method, __repr__ will be applied in the situations,
where __str__ would be applied, if it were available:
"""
class A:
    def __repr__(self):
        return "42"
a = A()
print(repr(a))
print(str(a))
print(a)

"""
A frequently asked question is when to use __repr__ and when __str__.
__str__ is always the right choice, if the output should be for the end user or in other words, if it should be nicely printed.
__repr__ on the other hand is used for the internal representation of an object.
The output of __repr__ should be - if feasible - a string which can be parsed by the python interpreter. The result of this parsing is in an equal object.
That is, the following should be true for an object "o":
        o == eval(repr(o))
"""
l = [3, 10, 13]
s = repr(l)
print(s)    # Output: [3, 10, 13]
print(l == eval(s))    # Returns True
print(l == eval(str(s)))    # Returns True

""" We show in the following example with the datetime module that eval can only be applied on the strings created by repr: """
import datetime
today = datetime.datetime.now()
str_s = str(today)
# print(eval(str_s))    # This returns an error
repr_s = repr(today)
t = eval(repr_s)
print(t)    # This returns the current date and time
print(type(t))    # Output: <class 'datetime.datetime'>
""" We can see that eval(repr_s) returns again a datetime.datetime object. The string created by str can't be turned into a datetime.datetime object by parsing it. """

""" We will extend our robot class with a repr method. We dropped the other methods to keep this example simple: """
"""
class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
    def __repr__(self):
        return "Robot('" + self.name + "', " +  str(self.build_year) +  ")"
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))
    new = eval(x_str) 
    print(new)
    print("Type of new:", type(new))
"""

"""
x_str has the value Robot('Marvin', 1979). eval(x_str) converts it again into a Robot instance.
Now it's time to extend our class with a user friendly __str__ method:
"""
"""
class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
    def __repr__(self):
        return "Robot('" + self.name + "', " +  str(self.build_year) +  ")"
    def __str__(self):
        return "Name: " + self.name + ", Build Year: " +  str(self.build_year)
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))
    new = eval(x_str)
    print(new)
    print("Type of new:", type(new))
"""

"""
When we start this program, we can see that it is not possible to convert our string x_str, created via str(x), into a Robot object anymore.
We show in the following program that x_repr can still be turned into a Robot object:
"""
class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
    def __repr__(self):
        return "Robot(\"" + self.name + "\"," +  str(self.build_year) +  ")"
    def __str__(self):
        return "Name: " + self.name + ", Build Year: " +  str(self.build_year)
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    x_repr = repr(x)
    print(x_repr, type(x_repr))
    new = eval(x_repr)
    print(new)
    print("Type of new:", type(new))


""" Public, - Protected-, and Private Attributes """
"""
- Private attributes should only be used by the owner, i.e. inside of the class definition itself.
- Protected (restricted) Attributes may be used, but at your own risk. Essentially, they should only be used under certain conditions.
- Public Attributes can and should be freely used.

Python uses a special naming scheme for attributes to control the accessibility of the attributes. So far, we have used attribute names,
which can be freely used inside or outside of a class definition, as we have seen. This corresponds to public attributes of course.
There are two ways to restrict the access to class attributes:
- First, we can prefix an attribute name with a leading underscore "_". This marks the attribute as protected. It tells users of the class
not to use this attribute unless, they write a subclass. We will learn about inheritance and subclassing in the next chapter of our tutorial.
- Second, we can prefix an attribute name with two leading underscores "__". The attribute is now inaccessible and invisible from outside.
It's neither possible to read nor write to those attributes except inside the class definition itself*.

Naming     Type         Meaning
name       Public       These attributes can be freely used inside or outside a class definition.
_name      Protected    Protected attributes should not be used outside the class definition, unless inside a subclass definition.
__name     Private      This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside the class definition itself.
"""
# Example:
class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
x = A()
print(x.pub)    # Output: 'I am public'
print(x.pub + " and my value can be changed")    # Output: 'I am public and my value can be changed'
print(x._prot)    # Output: 'I am protected'
# print(x.__priv)    # Returns: 'A' object has no attribute '__priv'. Did you mean: '_A__priv'?
# The error message is very interesting. One might have expected a message like "__priv is private". We get the message "AttributeError:
# 'A' object has no attribute __priv instead, which looks like a "lie". There is such an attribute, but we are told that there isn't.
# This is perfect information hiding. Telling a user that an attribute name is private, means that we make some information visible, i.e.
# the existence or non-existence of a private variable.

class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name    
    def set_build_year(self, by):
        self.__build_year = by
    def get_build_year(self):
        return self.__build_year    
    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"
    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")
# Every private attribute of our class has a getter and a setter. There are IDEs for object-oriented programming languages,
# who automatically provide getters and setters for every private attribute as soon as an attribute is created.



""" The Destructor """
"""
What we said about constructors holds true for destructors as well. There is no "real" destructor, but something similar, i.e. the method __del__.
It is called when the instance is about to be destroyed and if there is no other reference to this instance. If a base class has a __del__() method,
the derived class's __del__() method, if any, must explicitly call it to ensure proper deletion of the base class part of the instance.
"""
# The following script is an example with __init__ and __del__:
class Robot():
    def __init__(self, name):
        print(name + " has been created!")
    # This is just like initializing a delete method.
    def __del__(self):
        print ("Robot has been destroyed")
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y

"""
The usage of the __del__ method is very problematic. If we change the previous code to personalize the deletion of a robot, we create an error:
"""
class Robot():
    def __init__(self, name):
        print(name + " has been created!")
    def __del__(self):
        print (self.name + " says bye-bye!")
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y
"""
Output Error:
 print (self.name + " says bye-bye!")
           ^^^^^^^^^
AttributeError: 'Robot' object has no attribute 'name'
"""


""""
Additional Notes:
-----------------
"Objects are Python's abstraction for data. All data in a Python program is represented by objects or by relations between objects.
(In a sense, and in conformance to Von Neumann's model of a "stored program computer", code is also represented by objects.)
Every object has an identity, a type and a value." (excerpt from the official Python Language Reference)
"""

