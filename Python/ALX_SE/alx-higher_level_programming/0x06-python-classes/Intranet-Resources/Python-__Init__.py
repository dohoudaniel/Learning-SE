""" Python's __init__ method """
# A constructor is used initialize an object’s state. In Python, _init_ behaves like a constructor for a class.
# _init_ is called whenever a classes’ object is created.
# self represents a class’s instance and is required to access any variables or methods within the class.
class Code:
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print("Data is", self.data )

p = Code(3) ## Instance of class. 
p.print_data()
## __init__ is the first method that is called when you initilaze an object
## self is used to access the attribue data.

