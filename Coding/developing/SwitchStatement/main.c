#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,s;
char ch;
printf("Enter A for Addition:\n");

printf("Enter B for Substraction:\n");
scanf("%c",&ch); //after here will be the input of char
printf("Enter two numbers:");
scanf("%d %d",&a,&b);

switch(ch)
{

case 'A':
    s=a+b;
    printf("the result is:%d",s);
    break;

case 'B':
    s=a-b;
    printf("the result is:%d",s);
    break;
default:
    printf("INVALID!!!");
}
   return 0;
}
