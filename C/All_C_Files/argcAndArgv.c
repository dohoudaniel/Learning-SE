#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    int i, sum = 0;
    printf("argc = %d\n", argc);
    printf("Let us see what agrv[] does\n");
    
    if(argc > 1)
    {
        for(i = 1; i < argc; i++)
        {
            printf("argv[%d] = %s\n", i, argv[i]);
            sum += atoi(argv[i]); //This also means  sum = sum + atoi(argv[i]);
            //The atoi() function converts a chaacter string to an integer value
        }
        printf("Total = %d\n", sum);
    }

    return (0);
}
