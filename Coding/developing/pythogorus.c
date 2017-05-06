#include<stdio.h>
#include<math.h>

int main(){
	double a,b,c;
	printf("Enter the value of a &b:");

	scanf("%lf%lf",&a,&b);
   c=sqrt(pow(a,2)+pow(b,2));
   
   printf("So the hypothenus is:%lf",c);
	
	return 0;
	
}
