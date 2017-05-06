#include <iostream>

using namespace std;


int maximum (int,int,int);

main()
{
	int a,b,c;

   cout<<"Enter Three Integers: ";
   cin>>a>>b>>c;
   cout<<"Maximum is: "<<maximum(a,b,c)<<endl;

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
