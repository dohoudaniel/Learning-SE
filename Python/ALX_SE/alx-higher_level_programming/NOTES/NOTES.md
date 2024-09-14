My Notes:
-----------

print() statements
------------------
- The print() function prints the specified message to the screen, or other standard output device.
# Syntax:
	print(object(s), sep=separator, end=end, file=file, flush=flush)
- object(s)	Any object, and as many as you like. Will be converted to string before printed
- sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
- end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)
- file	Optional. An object with a write method. Default is sys.stdout
- flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False
