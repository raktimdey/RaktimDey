#include<stdio.h>
int main(){
    int year;

    printf("Enter any year: ");
    scanf("%d",&year);

    if(((year%4==0)&&(year%100!=0))||(year%400==0))
         printf("This is a leap year\n");
   
  else if(year%15==0){
 	printf("This is a huluculu festival year\n");
 }
 
 else if(year%55==0){
 printf("this is a Bulukulu festival\n");
 }
 else{
 	printf("this is an ordinary year\n");
 }
    return 0;
}
