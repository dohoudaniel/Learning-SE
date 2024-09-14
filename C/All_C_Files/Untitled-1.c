#include <stdio.h>

#define DANIEL 1, \
               2, \
               3, \
               4, \
               5, \
               6, \
               7


int main()
{
    int myArray[] = { DANIEL };

    printf("Dohou Daniel is:\n");
    
    for (int D = 0; D < 7; D++)
    {
    printf("%d ", myArray[D]);
    }
    return (0);
}
