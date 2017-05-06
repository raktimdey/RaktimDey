#include<stdio.h>

int main( )
	   {
         char k[100],ch;
         int c=0;
            do{
            ch=getchar();
            k[c]=ch;
            c++;
            }while (ch!='\n');
         c=c-1;
         k[c]='\0';
         printf("%s",k);


         return 0;
	    }
