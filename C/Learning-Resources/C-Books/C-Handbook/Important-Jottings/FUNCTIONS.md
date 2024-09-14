This file contains jottings on functions:
1. We can have multiple parameters, and if so we separate them using a comma, both in the declaration and in the invocation:

	void doSomething(int value1, int value2) {
	 /* ... */
	}
	doSomething(3, 4);

	- Parameters are passed by copy. This means that if you modify value1 , its value is modified locally, and the value outside of the function, where it was passed in the invocation, does not change.
	- If you pass a pointer as a parameter, you can modify that variable value because you can now access it directly using its memory address.
