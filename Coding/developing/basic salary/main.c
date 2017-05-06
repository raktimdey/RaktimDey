#include <stdio.h>
#include <stdlib.h>

int main()
{
    float basic,gross,hra,da;

    printf("Enter the amount of basic salary:\n");
    scanf("%f",&basic);

    if(basic<=10000){

     da=basic*0.8;
     hra=basic*0.2;
    }

    else if(basic<=20000){

    hra=basic*0.25;
    da=basic*0.9;
    }

    else if(basic>20000){

    hra=basic*0.35;
    da=basic*0.95;
    }

    gross=basic+hra+da;

    printf("So the gross amount is: %.2f ",gross);
    return 0;
}
