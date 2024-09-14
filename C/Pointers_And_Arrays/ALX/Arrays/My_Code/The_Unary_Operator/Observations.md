# My Observations

1. I noticed that if you try to print the address of a variable without using '&' (the unary operator), it prints a value, but if you try it again using the unary operator, it gives you the address, in memory, of that variable.
2. Also, if you try to print the address of an array without using '&' (the unary operator), it prints the address of the array, and also, if you try it again using the unary operator, you still print the address of the array.
- Also remember, printing the address of an array using the array name and the first index of an array, it prints the same value -> The address of the array.

3. For Array.c, as a consequence, the value of Daniel, is the same as the value of &Daniel. But they do not have the same type:
	- Daniel: in this context, general rule applies, so using Daniel will be evaluated as the address of the first element of the array. Thus, Daniel is of type char *
	- &Daniel: in this context (one of the two exceptions to the general rule), Daniel will be evaluated as the array object itself. so Daniel is of type char[98] - an array of 98 characters - and then &Daniel is of type char (*)[98], a pointer to an array of 98 characters.
- This is really important to note.
