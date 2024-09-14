# Notes
1. The help() function is used to check out the documentation (docstring) and more information of a function or a class. It's syntax is:
- 	help(ClassName)
	help(FunctionName)
2. There is a difference between `/` and `//` in Python.
- The `//` operator, also known as or for 'Floor Division', when used, returns the int quotient of the division.
	Example:    >>> print(5 // 2)
	            2
- The `/` operator returns the exact solution no matter if it's a float type or something.
	Example:    >>> print(5 / 2)
	            2.5
3. The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError. You can write a message to be written if the code returns False.
4. Take a look at this code:
	class Daniel(object):
	    def __init__(self, x):
	        ~~~~~~~~~~~~~~~~~
		~~~~~~~~~~~~~~~~~

	    def __str__(self):
	        ~~~~~~~~~~~~~~

	- When the __str__ method is defined in a class, it tells Python that whenever a print statement is called on an object that is of type 'ClassName', it must call the __str__ method for that object instance.
