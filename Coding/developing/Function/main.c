#include <stdio.h>
#include <conio.h>

int maximum (int,int,int);

int main()
{
	int a,b,c;

   printf("Enter Three Integers: ");
   scanf("%d%d%d",&a,&b,&c);
   printf("Maximum is:%d ",maximum);
   getch();
   return 0;
}

int maximum (int a,int b,int c)
{
   if(a>b)
   {
      if(a>c)
      {
         return a;
      }
   }
   else if(b>a)
   {
      if(b>c)
      {
         return b;
      }
   }
   else if(c>b)
   {
   	if(c>a)
      {
      	return c;
      }
   }
}
