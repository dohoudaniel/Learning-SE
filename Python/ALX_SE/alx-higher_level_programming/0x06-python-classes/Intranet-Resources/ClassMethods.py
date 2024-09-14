# Class Methods
# -------------

# The classmethod() method returns a class method for the given function. Example:
class Student:
  marks = 0

  def compute_marks(self, obtained_marks):
    marks = obtained_marks
    print('Obtained Marks:', marks)

# convert compute_marks() to class method
Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(88)

# Output: Obtained Marks: 88


"""
    classmethod syntax
-->        classmethod(function)
classmethod() is considered un-Pythonic, so in newer Python versions, you can use the @classmethod decorator for classmethod definition.
    The syntax is:
-->        @classmethod
           def func(cls, args...)

    classmethod() parameters
classmethod() method takes a single parameter:
function - Function that needs to be converted into a class method

    classmethod() Return Value
classmethod() method returns a class method for the given function.

    What is a classmethod?
    ----------------------
A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod.

The difference between a static method and a class method is:
- Static method knows nothing about the class and just deals with the parameters
- Class method works with the class since its parameter is always the class itself.

The class method can be called both by the class and its object.
    Class.classmethod()
Or even
    Class().classmethod()

But no matter what, the class method is always attached to a class with the first argument as the class itself cls.
        def classMethod(cls, args...)
"""

# cls accepts the class as a parameter rather than class' object/instance.

