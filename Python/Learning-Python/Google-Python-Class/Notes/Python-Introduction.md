Notes On Python Introduction:
-----------------------------
- #!/usr/bin/python3
- python3 pythonfile.py pythonOutputFile
- Python source files use the ".py" extension and are called "modules." With a Python module hello.py, the easiest way to run it is with the shell command "python hello.py Alice" which calls the Python interpreter to execute the code in hello.py, passing it the command line argument "Alice".
- When a Python file is run directly, the special variable "__name__" is set to "__main__". Therefore, it's common to have the boilerplate if __name__ ==... shown above to call a main() function when the module is run directly, but not when the module is imported by some other module.
- In a standard Python program, the list sys.argv contains the command-line arguments in the standard way with sys.argv[0] being the program itself, sys.argv[1] the first argument, and so on.
- * is Python's "repeat" operator.
- Both + and * are called "overloaded" operators because they mean different things for numbers vs. for strings (and other data types).
- At run time, functions must be defined by the execution of a "def" before they are called. It's typical to def a main() function towards the bottom of the file with the functions it calls above it.


# Indentation:
- One unusual Python feature is that the whitespace indentation of a piece of code affects its meaning. A logical block of statements such as the ones that make up a function should all have the same indentation, set in from the indentation of their parent function or "if" or whatever. If one of the lines in a group has a different indentation, it is flagged as a syntax error.

Python's use of whitespace feels a little strange at first, but it's logical and I found I got used to it very quickly. Avoid using TABs as they greatly complicate the indentation scheme (not to mention TABs may mean different things on different platforms). Set your editor to insert spaces instead of TABs for Python code.

A common question beginners ask is, "How many spaces should I indent?" According to the official Python style guide (PEP 8), you should indent with 4 spaces. (Fun fact: Google's internal style guideline dictates indenting by 2 spaces!)


# Modules and Namespaces:
- We have the standard "sys" module that contains some standard system facilities, like the argv list, and exit() function. With the statement "import sys" you can then access the definitions in the sys module and make them available by their fully-qualified name, e.g. sys.exit(). (Yes, 'sys' has a namespace too!)
- There is another import form that looks like this: "from sys import argv, exit". That makes argv and exit() available by their short names; however, we recommend the original form with the fully-qualified names because it's a lot easier to determine where a function or attribute came from.
- There are many modules and packages which are bundled with a standard installation of the Python interpreter, so you don't have to do anything extra to use them. These are collectively known as the "Python Standard Library." Commonly used modules/packages include:
	- ```sys — access to exit(), argv, stdin, stdout, ...```
	- ```re — regular expressions```
	- ```os — operating system interface, file system```

# The help() and the dir() functions
- Inside the Python interpreter, the help() function pulls up documentation strings for various modules, functions, and methods. These doc strings are similar to Java's javadoc. The dir() function tells you what the attributes of an object are.
