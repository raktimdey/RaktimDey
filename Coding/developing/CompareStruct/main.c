#include <stdio.h>

struct student
	{
	char name[20];
	char address[20];
	int roll;
	int cn;
	}a[25];
void main ()
{	int i;
	clrscr();
	for (i=0; i<25; i++)
	scanf(“%s %s %d %f”, &a[i].name , &a[i].address ,&a[i].roll,&a[i].cn);

}
