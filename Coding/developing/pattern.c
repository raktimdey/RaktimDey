#include <stdio.h>

int main() {
	int i,j;
	for(i=0;i<=5;i++){
		
		for(j=0;j<i;j++){
			printf("*",j);
		}
		printf("\n");
	}
	printf("Hello world!\n");
	return 0;
}
