#include <stdio.h>
#include <stdlib.h>

int addition(int x,int y);


int main()
{
    int one,two;
    printf("Enter the two numbers:");
    scanf("%d%d",&one,&two);
   // int store;
  //  store=addition(one,two);
    printf("So the sum is: %d ",addition(one,two));
    return 0;
}

int addition(int x,int y){

int sum;

sum=x+y;
return sum;

}

