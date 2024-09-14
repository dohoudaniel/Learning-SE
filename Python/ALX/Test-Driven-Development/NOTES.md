# Running Python Tests...

# doctest for python files (.py) using testmod()
- python3 pythonFile.py -v .: For this to work, don't forget to add:
	- if __name__ == "__main__":
	-     import doctest
	-     doctest.testmod()
- python -m doctest -v pythonFile.py : This is a command line shortcut for running testmod(). This instructs the Python interpreter to run the doctest module directly from the standard library and You can pass the module name(s) on the command line.

# doctest for text files (.txt) using testfile()
-	`import doctest()`
- 	`doctest.testfile("exampleFile.txt")`
	This script executes and verifies any interactive Python examples contained in the file exampleFile.txt.
- There is also a command line shortcut for running testfile(). You can instruct the Python interpreter to run the doctest module directly from the standard library and pass the file name(s) on the command line:
	- python -m doctest -v example.txt
    Because the file name does not end with .py, doctest infers that it must be run with testfile(), not testmod().
