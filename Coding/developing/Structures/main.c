#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE*p1,*p2;
    int a;
    int b;
    p1=fopen("really.txt","wt");
    p2=fopen("okay.txt","wt");
    fscanf(p1,"%d%f",&a,&b);
      fscanf(p2,"%d%f",&a,&b);

    return 0;
}
