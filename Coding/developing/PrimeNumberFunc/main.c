#include <stdio.h>
#include <stdlib.h>

int PrimeNumber(int n);
int main()
{
    int n,flag;
    printf("Enter a positive number: ");
    scanf("%d",&n);

    flag=PrimeNumber(n);

    if(flag==1){
        printf("%d is a prime number.\n",n);
    }else{
      printf("%d is not a prime number.\n",n);
    }
    return 0;
}

int PrimeNumber(int n){

 int i, flag=1;

 for(i=2;i<=n/2;i++){

    if(n%i==0){
        flag=0;
    }
 }
return flag;
}
