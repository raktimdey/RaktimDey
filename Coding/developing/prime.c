#include<stdio.h>
#include<conio.h>
#include <stdbool.h>

bool isPrimeNumber(int input);

int main(){

  int input,i;

  printf("enter any number:");
  scanf("%d",&input);

if(isPrimeNumber(input)){
    printf("%d is a prime number",input);
}
else
    printf("%d isnt prime number",input);

return 0;
}

bool isPrimeNumber(int input){

int i;
for(i=2;i<input;i++){
    if(input%i==0)
    break;
  }
  if(i==input){
   return true;
}
else{
    return false;
}
}
