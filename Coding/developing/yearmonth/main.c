#include <stdio.h>
#include <stdlib.h>

int main()
{
   int day,month,weeks,years;
       printf("Enter the number of days:");
       scanf("%d",&day);
       years=day/365;
       month=day/30;
       weeks=day/7;
    
	   day=day%7;

       printf("Number in years:%d\n",years);
        printf("Number in months:%d\n",month);
         printf("Number in weeks:%d\n",weeks);
          printf("Number in day:%d\n",day);
       


       return 0;
}
