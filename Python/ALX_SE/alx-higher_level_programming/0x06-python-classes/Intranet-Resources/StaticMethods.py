"""
Python Static Methods
Link: https://pynative.com/python-class-method/
"""

# Static method: It is a general utility method that performs a task in isolation. Inside
# this method, we don’t use instance or class variable because this static method doesn’t
# take any parameters like self and cls.
# A static method is bound to the class and not the object of the class. Therefore, we can call it using the class name.
# A static method doesn’t have access to the class and instance variables because it does not receive an implicit first
# argument like self and cls. Therefore it cannot modify the state of the object or class.
# The class method can be called using ClassName.method_name() as well as by using an object of the class.
class Employee:
    @staticmethod
    def sample(d):
        print("Inside a static method is", d)

# calling the static method
Employee.sample(10)
# It can also be called using an object
ant = Employee()
ant.sample(100)

# Defining a static method in Python
# Any method we create in a class will automatically be created as an instance method.
# We must explicitly tell Python that it is a static method using the @staticmethod decorator or staticmethod() function.
# Syntax:        class C:
#                    @staticmethod
#                    def f(arg1, arg2, ...): ...
""" Creating Static Method Using @staticmethod Decorator """
# To make a method a static method, add @staticmethod decorator before the method definition.
# The @staticmethod decorator is a built-in function decorator in Python to declare a method as a static method.
# It is an expression that gets evaluated after our function is defined.
class Employees(object):
    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)

emp = Employees('Kelly', 12000, 'ABC Project')
emp.work()

"""
Advantages of a Static Method:
1. Consume Less memory: Instance methods are object too, and creating them has a cost.Having a static method avoids that.
Let’s assume you have ten employee objects and if you create gather_requirement() as a instance method then Python have to
create a ten copies of this method (seperate for each object) which will consume more memeory.
On the other hand static method has only one copy per class.
"""
kelly = Employees('Kelly', 12000, 'ABC Project')
jessa = Employees('Jessa', 7000, 'XYZ Project')
# false
# because seperate copy of instance method is created for each object
print(kelly.work is jessa.work)
# True because only one copy is created. kelly and jess objects share the same methods
print(kelly.gather_requirement is jessa.gather_requirement)
# True
print(kelly.gather_requirement is Employees.gather_requirement)
"""
2. To Write Utility functions: Static methods have limited use because they don’t have access to the attributes of an object
(instance variables) and class attributes (class variables). However, they can be helpful in utility such as conversion from
one type to another. The parameters provided are enough to operate.
3. Readabiltity: Seeing the @staticmethod at the top of the method, we know that the method does not depend on the object’s
state or the class state.
"""

""" The staticmethod() function """
# You should only use staticmethod() function to define static method if you have to support older versions of Python (2.2 and 2.3).
# Otherwise, it is recommended to use the @staticmethod decorator.
# Syntax:        staticmethod(function)
# - function: It is the name of the method you want to convert as a static method.
# - It returns the converted static method.
class Dan:
    def dohou(x):
        print('Inside a static method is', x)
# convert to a static method
Dan.dohou = staticmethod(Dan.dohou)
# calling a static method
Dan.dohou(10)
# The staticmethod() approach is helpful when you need a reference to a function from a class body and you want to avoid the automatic
# transformation to the instance method.

""" Call A Static Method from Another Method """
class Test :
    @staticmethod
    def static_method_1():
        print('This is static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()

# call class method
Test.class_method_1()

