#include <stdio.h>

int main(void)
{
	int a = 100;
    int b = 2;
    int c = 25;
    int d = 4;
    int result;
    
    result = a - b;
    printf("a - b = %i\n", result);
    
    result = a * b;
    printf("a * b = %i\n", result);
    
    result = a / c;
    printf("a / c = %i\n", result);
    
    result = a + b * c;    //Precedence works here.
    printf("a + b * c = %i\n", result);    // b * c will be calculated first.
	
	printf("a * b + c * d = %i\n", a * b + c * d);
    
    return ();
}

