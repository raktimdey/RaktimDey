#include <stdio.h>
#include <stdlib.h>

int findarea(int x,int y);

int main()
{
    int one,two;
    scanf("%d%d",&one,&two);
    printf("%d",findarea(one,two));
    return 0;
}

int findarea(int x,int y){

return x*y;
}
