//Function Pointers And Callbacks
#include <stdio.h>

void A()
{
	printf("Hello Daniel :)");
}

void B(void (*ptr)()) //B takes a function pointer as an argument
{
	ptr(); //call-back function that 'ptr' points to ( I think it is A)
}

int main()
{
	void (*p)() = A;
	B(p);
	B(A); //Name of a function also returns a pointer.

//When reference to a function is passed into another function, then that particular function is called a Call-back function
//In the above example, A is a callback function, that is called back by B througn the reference (funtion pointer)
}
