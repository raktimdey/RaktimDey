#include <stdio.h>

void main(){
	
	int x,y;
	int *p;
	x=10;
	p=&x;
	y=*p;
	printf("%d\n",x); 
	printf("%u\n",p);
	printf("%d\n",y);
	*p=200;
	printf("%d\n",x);
	
}
