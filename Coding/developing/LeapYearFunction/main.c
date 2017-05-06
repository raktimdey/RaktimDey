#include <stdio.h>
#include <stdlib.h>

int main(){
 int year;

 printf("Enter a year: ");

 if(year%4==0 && year%100!==0||year%400==0){

    printf("this is a leap year");
 }
 else if(year%15==0){
    printf("This is a huluculu festival year");
 }
 else if(year%55==0){
    printf("This is a Bulukulu festival");
 }
 else{
    printf("this is an ordinary year");
 }


return 0;

}
