#include <stdio.h>
#include <stdlib.h>

int incrementAge()
{
	int age = 0;
	age++;
	return age;
		/* 
		 * If we call incrementAge() once, we'll get 1 as the return value. If we call it
		 * more than once, we'll always get 1 back, because age is a local variable and
		 * it's re-initialized to 0 on every single function call.
		 */
}

int IncrementAge()
{
	static int Age = 0;
	Age++;
	return Age;
		/*
		 * Now every time we call this function, we'll get an incremented value.
		 * We can also omit initializing age to 0 in static int age = 0; , and just
		 * write static int age; because static variables are automatically set to 0
		 * when created.
		 */
}

int main()
{
	incrementAge();
	IncrementAge();
}
