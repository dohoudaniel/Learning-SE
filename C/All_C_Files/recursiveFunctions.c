#include <stdio.h>
#include <stdlib.h>

void print(int nb)
{
        printf("%d\n", nb);
        --nb;
        if (nb >= 0)
        {
            print(nb);
        }
}

int main(void)
{
        print(10);
        return (0);
}
