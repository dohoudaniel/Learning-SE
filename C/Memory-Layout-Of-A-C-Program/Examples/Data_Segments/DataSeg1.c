#include <stdio.h>
/**
 * Demonstration of an initialized read-write area of the data segment.
 */
char str[]= "Amlendra Kumar";

int main(void)
{
        printf("%s\n",str);

        str[0]='k';

        printf("%s\n",str);

        return (0);
}

/**
 * You can see the above example str is a global array, so it will go in the data segment (DS).
 * You can also see that I am able to change the value so it has read and write permission.
 */
