"""
Python - Understanding self and __init__ method in python Class.
Link: https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
"""
""" Definitions """
# Class: Class is a set or category of things having some property or attribute in common and differentiated from others by kind, type, or quality.
# In technical terms we can say that class is a blue print for individual objects with exact behaviour.

# Object: object is one of instances of the class. which can perform the functionalities which are defined in the class.

# self: self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.

# __init__: "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when
# an object is created from the class and it allow the class to initialize the attributes of a class.
class Car(object):
    """
    blueprint for car
    """

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating...")
        "accelarator functionality here"
    def change_gear(self, gear_type):
        print("gear changed")
        " gear related functionality here"

# creating different types of cars
maruthi_suzuki = Car("Ertiga", "Black", "Suzuki", 60)
audi = Car("A6", "Red", "Audi", 80)
"""
We have created two different types of car objects with the same class. while creating the car object we passed arguments
"Ertiga", "Black", "Suzuki", '60'  these arguments will pass to "__init__" method  to initialize the object.
Here, the magic keyword "self"  represents the instance of the class. It binds the attributes with the given arguments.
"""


# Case 1: Find out the cost of a rectangular field with breadth(b=120), length(l=160). It costs x (2000) rupees per 1 square unit
class Rectangle:
    def __init__(self, length, breadth, unitCost):
        self.length = length
        self.breadth = breadth
        self.unitCost = unitCost

    # The method for the area
    def area(self):
        return (self.length * self.breadth)

    # The method for the perimeter
    def perimeter(self):
        return 2 * (self.length + self.breadth)

    # The method for the unit cost
    def cost(self):
        area = self.area()
        return area * self.unitCost

problem = Rectangle(160, 120, 2000)
print("The area of the rectangle is {}cm^2.".format(problem.area()))
print("The perimeter of the rectangle is {}cm.".format(problem.perimeter()))
print("The cost per unit area is {} cm^2.".format(problem.cost()))

