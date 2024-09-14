"""
Python Class Methods
Link: https://pynative.com/python-class-method/
"""

# Class method: Used to access or modify the class state. In method implementation, if we
# use only class variables, then such type of methods we should declare as a class method.
# The class method has a cls parameter which refers to the class.

# Class methods are methods called on the class itself, not on a specific object instance.
# Therefore, it belongs to a class level, and all class instances share a class method.
# A class method is bound to the class and not the object of the class. It can access only class variables.
# It can modify the class state by changing the value of a class variable that would apply across all the class objects.
# In method implementation, if we use only class variables, we should declare such methods as class methods.
# The class method has a cls as the first parameter, which refers to the class.
# Class methods are used when we are dealing with factory methods.
#  Factory methods are those methods that return a class object for different use cases. Thus, factory methods create
# concrete implementations of a common interface.
# Example:
class Student:
    school_name = 'Prestige Private College'    # A Class variable

    def __init__(self, name, age):    # The constructor to initialize instance variables
        self.name = name
        self.age = age

    """ The Class Method """
    @classmethod
    def change_school(cls, name):    # cls refers to the class name
        print(Student.school_name)    # Accessing the class variables
        Student.school_name = name    # Modifying class variables

jesse = Student('Jesse', 15)
Student.change_school('A Beautiful Mind')

# Any method we create in a class will automatically be created as an instance method. So,
# We must explicitly tell Python that it is a class method using the @classmethod decorator or classmethod() function.
# Like, inside an instance method, we use the self keyword to access or modify the instance variables. Same inside the class method,
# we use the cls keyword as a first parameter to access class variables. Therefore the class method gives us control of changing the class state.

"""
Example 1: Create Class Method Using @classmethod Decorator
"""
# The @classmethod decorator is a built-in function decorator. In Python, we use the @classmethod decorator to declare a method as a class method.
# The @classmethod decorator is an expression that gets evaluated after our function is defined.
from datetime import date

class Daniel:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate an age and set it as an age
        # Return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "\'s age is: " + str(self.age))


# Initialization
barry = Daniel('Barry', 20)
barry.show()

# create new object using the factory method
joy = Daniel.calculate_age("Joy", 1995)
joy.show()

"""
Explanation:
------------
- In the above example, we created two objects, one using the constructor and the second using the calculate_age() method.
- The constructor takes two arguments name and age. On the other hand, class method takes cls, name, and birth_year and
returns a class instance which nothing but a new object.
- The @classmethod decorator is used for converting calculate_age() method to a class method.
- The calculate_age() method takes Student class (cls) as a first parameter and returns constructor by calling Student(name, date.today().year - birthYear),
which is equivalent to Student(name, age).
"""


"""
Example 2: Create Class Method Using classmethod() function
"""
# The built-in function classmethod() is used to convert a normal method into a class method. The classmethod() is an inbuilt function in Python, which returns
# a class method for a given function.
# Syntax:             classmethod(function)
# function: It is the name of the method you want to convert as a class method.
# It returns the converted class method.
# Note: The method you want to convert as a class method must accept class (cls) as the first argument, just like an instance method receives the instance (self).
class Beautiful:
    # a class variable
    name = "A Mind"

    def schoolName(cls):
        print("School name is:", cls.name)

# creating a classmethod
Beautiful.schoolName = classmethod(Beautiful.schoolName)
# calling the classmethod
Beautiful.schoolName()


"""
Example 3: Accessing class variables in class methods
"""
# Using the class method, we can only access or modify the class variables. Let’s see how to access and modify the class variables in the class method.
# Class variables are shared by all instances of a class.
# Using the class method we can modify the class state by changing the value of a class variable that would apply across all the class objects.
class school:
    studentTime = 'Peace'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def ChangeSchool(cls, studentTime):
        # class_name.class_variable
        cls.studentTime  = studentTime

    # instance method
    def show(self):
        print(self.name, self.age, 'School:', school.studentTime)

# Initialization
daniel = school('Daniel', 16)
daniel.show()
# change studentTime
school.ChangeSchool('Promise')
daniel.show()


""" Class Methods In Inheritance """
# In inheritance, the class method of a parent class is available to a child class.
# Example:
class Vehicle:
    brand_name = "BMW"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_price(cls, name, price):
        # ind_price = dollar * 75
        # create a new vehicle object
        return cls(name, (price * 75))

    def show(self):
        print(self.name, self.price)


# The class Car inherits its attributes from the Vehicle class, that is why Vehicle is in brackets
class Car(Vehicle):
    def average(self, distance, fuel_used):
        mileage = distance / fuel_used
        print(self.name, 'Mileage', mileage)


bmw_us = Car('BMW X5', 65000)
bmw_us.show()

# The class method of the parent class is available to the child class
# This object will return the object of the calling class
bmw_ind = Car.from_price('BMW X600', 65000)
bmw_ind.show()


# Check the type
print(type(bmw_ind))


""" Dynamically Add Class Method to a Class """
class Students:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)
# class ended

# Adding a method outside class
def exercises(cls):
    # access class variables
    print("Below exercises for", cls.school_name)

# Adding class method at runtime to class
Students.exercises = classmethod(exercises)

jessa = Students("Jessa", 14)
jessa.show()
# call the new method
Students.exercises()



""" Dynamically Delete Class Methods """
# We can dynamically delete the class methods from the class. In Python, there are two ways to do it:
# - By using the del operator
# - By using delattr() method

""" # By using the del operator """
# The del operator removes the instance method added by class.
# Use the del class_name.class_method syntax to delete the class method.
class Guts:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        cls.school_name = school_name

jessa = Guts('Jessa', 20)
Guts.change_school('XYZ School')

# delete class method
# del Guts.change_school
# call class method
# it will return an error
# Guts.change_school('PQR School')

"""By using delattr() method  """
# The delattr() method is used to delete the named attribute and method from the class.
# The argument to delattr is an object and string. The string must be the name of an attribute or method name.
don = Guts('Jessa', 20)
don.change_school('XYZ School')
# delete class method
# Syntax:        delattr(class, class method)
# delattr(Guts, 'change_school')
# call class method
# it will return an error
# don.change_school('PQR School')

