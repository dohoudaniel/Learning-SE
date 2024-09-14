# Object Oriented Programming - Classes
# 0x06-python_classes

# The __init__ method
class Favour:
    def __init__(self, name):
        self.name = name
        
        
    def say_hi(self):
        print("Hello, I am", self.name)

g = Favour('Barry Allen')
g.say_hi()    # Output: Hello, I am Barry Allen
"""
Here, we define the __init__ method as taking a parameter name (along with the usual self). Here, we just create a new field also called name.
Notice these are two different variables even though they are both called 'name'. There is no problem because the dotted notation self.name
means that there is something called "name" that is part of the object called "self" and the other name is a local variable. Since we explicitly
indicate which name we are referring to, there is no confusion.
When creating new instance g, of the class Person, we do so by using the class name, followed by the arguments in the parentheses: g = Favour('Barry Allen').
We do not explicitly call the __init__ method. This is the special significance of this method.
Now, we are able to use the self.name field in our methods which is demonstrated in the say_hi method.
"""

