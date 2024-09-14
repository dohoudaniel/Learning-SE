# Object Oriented Programming - Classes
# 0x06-python_classes

# Classes
class Daniel:
    pass    # An empty block
p = Daniel()
print(p)    # Output: <__main__.Daniel object at 0x00000230F24C6D10>
"""
We create a new class using the class statement and the name of the class. This is followed by an indented block of statements which form the
body of the class. In this case, we have an empty block which is indicated using the pass statement.
Next, we create an object/instance of this class using the name of the class followed by a pair of parentheses. For our verification, we confirm
the type of the variable by simply printing it. It tells us that we have an instance of the Daniel class in the __main__ module.
Notice that the address of the computer memory where your object is stored is also printed. The address will have a different value on your
computer since Python can store the object wherever it finds space.
"""

