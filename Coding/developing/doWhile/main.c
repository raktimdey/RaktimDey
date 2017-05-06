#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,s;
    s=0;
    do{
        s=s+i;
        i++;
    }while(i<100);
    printf("The summation of o to 99 is: %d",s);
    return 0;
}
