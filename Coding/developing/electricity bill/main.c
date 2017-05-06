#include <stdio.h>
#include <stdlib.h>

int main()
{
   int unit;
   float amount,tamount,surcharge;

   printf("enter the amount of units:");
   scanf("%d",&unit);

   if(unit<=50){

   amount=unit*0.50;

   }
   else if(unit<=100){
   amount=25+((unit-50)*0.75);
   }
   else if(unit<=250){

     amount=100+((unit-150)*1.20);
   }

   else if(unit>250){

      amount=220+((unit-250)*1.80);

   }

   surcharge=amount*0.20;
   tamount=amount+surcharge;

   printf("\nElectricity Bill= Rs.%.2f",tamount);
    return 0;
}
