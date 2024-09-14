- Lists are mutable.
- You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 1 This is a design principle for all mutable data structures in Python.

# Using lists as stacks
- The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index.

# Using lists as queues
- It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one). To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

# The round() function
- The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
 The default number of decimals is 0, meaning that the function will return the nearest integer if the number of decimal is not specified.
	Syntax:
	round(number, digits)
	- number - Required, the number to be rounded
	- digits - Optional, The number of decimals to use when rounding the number, the default is zero (0).
	
	Example:
	>>> x = round(12.58691, 3)
	>>> print(x)
		12.587

- Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
- Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking, or indexing (or even by attribute in the case of namedtuples).
