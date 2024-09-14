"""
Python Instance Methods
Link: https://pynative.com/python-class-method/
"""

# Instance Method: Used to access or modify the object state.
# If we use instance variables inside a method, such methods are called instance methods.
# It must have a self parameter to refer to the current object.
    
# If we use instance variables inside a method, such methods are called instance methods.
# The instance method performs a set of actions on the data/value provided by the instance variables.
# A instance method is bound to the object of the class.
# It can access or modify the object state by changing the value of a instance variables
# Any method we create in a class will automatically be created as an instance method unless we explicitly tell Python that it is a class or static method.
# Instance variables are not shared between objects. Instead, every object has its copy of the instance attribute. Using the instance method, we can access
# or modify the calling object’s attributes.
# Instance methods are defined inside a class, and it is pretty similar to defining a regular function.
# Use the def keyword to define an instance method in Python.
# Use self as the first parameter in the instance method when defining it. The self parameter refers to the current object.
# Using the self parameter to access or modify the current object attributes.
# You may use a variable named differently for self, but it is discouraged since self is the recommended convention in Python.
class Students:
    # constructor
    def __init__(self, name, sex, age):
        # Instance variables
        self.name = name
        self.sex = sex
        self.age = age

    # Instance method to access instance variable
    def details(self):
        print('Name:', self.name, '\nSex:', self.sex, '\nAge:', self.age)

    """ Modify Instance Variables inside Instance Method """
    def update_details(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
            
""" Calling Instance methods """
# Creating the first object
print("First Student")
print("-------------")
print('Details: ')
dan = Students('Dohou Daniel', 'Male', '16')
# Calling the instance method
dan.details()
print()

# Creating the second object
print('Second Student')
print("-------------")
print('Details: ')
mish = Students('Dohou Mishael', 'Male', '13')
# Calling the instance method
mish.details()
print()

""" Modifying instance variables """
print('Third Student')
print("-------------")
print('Details: ')
jeh = Students('10', 'Akpan Jehiel', 'Female')
jeh.details()
print('Oops....\nMistake In Database!...')
print('Updating Class Details.........')
print('Updating Third Student...')
print('Third Student')
print('Third Student Updated!')
print("----------------------")
print('Details: ')
jeh.update_details('Dohou Jehiel', '10', 'Male')
jeh.details()

""" Creating Instance Variables In Instance Method """
# Till the time we used constructor to create instance attributes. But, instance attributes are not specific only to the __init__() method;
# they can be defined elsewhere in the class.
class Blues:
    def __init__(self, rollNum, name, age):
        # Instance variable
        self.rollNum = rollNum
        self.name = name
        self.age = age

    # Instance methhod to add instance variable
    def add_marks(self, marks):
        # Add new attributes to the current object
        self.marks = marks

# Creating the object
zoom = Blues(20, "Barry", '20')
# Calling the instance method
zoom.add_marks(100)
# Display the object:
print('Roll Number:', zoom.rollNum, '\nName:', zoom.name, '\nAge:', zoom.age, '\nMarks:', zoom.marks)

""" Dynamically Add Instance Method to a Object """
# Usually, we add methods to a class body when defining a class.
# However, Python is a dynamic language that allows us to add or delete instance methods at runtime. Therefore, it is helpful in the following scenarios:
# When class is in a different file, and you don’t have access to modify the class structure
# You wanted to extend the class functionality without changing its basic structure because many systems use the same structure.
# Example:
# We should add a method to the object, so other instances don’t have access to that method.
# We use the types module’s MethodType() to add a method to an object.
import types
class Dim:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def sims(self):
        print("Name:", self.name, "\nAge:", self.age)
# Creating a new method
def tabs(self):
    print("Hello", self.name, ".\nWelcome to our home")
# create an object
s1 = Dim('Dimple', 2)
# Add instance method to an object
s1.tabs = types.MethodType(tabs, s1)
# Call the newly added method
s1.tabs()



""" Dynamically Delete Instance Methods """
# We can dynamically delete the instance method from the class. In Python, there are two ways to delete method:
# - By using the del operator
# - By using delattr() method

# By using the del operator
# The del operator removes the instance method added by class.
# Example: Delete the method from class using del operator
# del s1.tabs
# # Again calling the tabs method
# It will return an error
# s1.tabs()

# By using the delattr() method
# The delattr() is used to delete the named attribute from the object with the prior permission of the object.
# Use the following syntax to delete the instance method.
# Syntax:           delattr(object, name)
# - object: the object whose attribute we want to delete.
# - name: the name of the instance method you want to delete from the object.
# Example:
emma = Dim("John", 30)
emma.sims()
# delete instance method sims() using delattr()
# delattr(emma, 'tabs')
emma.sims()   # This shows that 'emma; is not deleted
# Again calling tabs method
# It will return an error
# emma.tabs()

