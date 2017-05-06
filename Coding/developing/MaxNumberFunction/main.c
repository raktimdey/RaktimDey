#include <stdio.h>
#include <stdlib.h>

int max(int x,int y,int z);
int main()
{
    int a,b,c;
    printf("take threee numbers:");
    scanf("%d%d%d",&a,&b,&c);
    int store;
    store=max(a,b,c);
    printf("Print the maximum number: %d",store);
    return 0;
}

int max(int x,int y,int z){

int result;

if(x>y && x>z){
    result= x;
}else if(y>x && y>z){

   result =y;
}else{
   result=z;
}
return result;
}
