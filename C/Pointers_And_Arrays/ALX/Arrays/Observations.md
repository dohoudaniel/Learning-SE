# My Observations

1. I noticed that if you try to print the address of a variable without using '&' (the unary operator), it prints a value, but if you try it again using the unary operator, it gives you the address, in memory, of that variable.
2. Also, if you try to print the address of an array without using '&' (the unary operator), it prints the address of the array, and also, if you try it again using the unary operator, you still print the address of the array.
- Also remember, printing the address of an array using the array name and the first index of an array, it prints the same value -> The address of the array.

3. For 18-main.c, as a consequence, the value of b, is the same as the value of &b. But they do not have the same type:
	- b: in this context, general rule applies, so using b will be evaluated as the address of the first element of the array. Thus, b is of type char *
	- &b: in this context (one of the two exceptions to the general rule), b will be evaluated as the array object itself. so b is of type char[98] - an array of 98 characters - and then &b is of type char (*)[98], a pointer to an array of 98 characters.
- This is really important to note because when we will manipulate those two pointers, they will behave differently, since the size of their type is different:
	- sizeof b is 98 (in 14-main.c)
	- sizeof &b is 8, (if you are using a regular 64 bits machine, as demonstrated in 19-main.c)
