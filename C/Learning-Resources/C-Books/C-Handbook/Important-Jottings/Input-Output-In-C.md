The C Handbook - Input/ Output
- #include <stdio.h>
	- This library provides us, among many other functions:
		- printf()
		- scanf()
		- sscanf()
		- fgets()
		- fprintf()

- We have three kinds of Input/Output streams:
	- stdin (Standard Input)
	- stdout (Standard Output)
	- stderr (Standard Error)

- A stream is a high level interface that can represent a device or a file. From the C standpoint, we don't have any difference in reading from a file or reading from the command line: it's an I/O stream in any case.

- printf() : prints characters to stdout
