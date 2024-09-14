- The typedef keyword in C allows you to defined new types.
- Starting from the built-in C types, we can create our own types, using this syntax:
	```typedef existingtype NEWTYPE;```
	The new type we create is usually, by convention, uppercase.
	This it to distinguish it more easily, and immediately recognize it as type.
	For example we can define a new NUMBER type that is an int :
	```typedef int NUMBER;```
- Well, typedef gets really useful when paired with two things: enumerated types and structures.
