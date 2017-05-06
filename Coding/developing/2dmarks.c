#include<stdio.h>

int main(){
	
	int s[4][3],t[4],tmp;
	int i,j;
	
	for(i=0;i<4;i++){
		printf("Enter three subjects marks for Student no:%d\n",i);
		
		for(j=0;j<3;j++){
			scanf("%d",&s[i][j]);
		}
		
	}
for(i=0;i<4;i++){
		printf("\n");
		
		for(j=0;j<3;j++){
			printf("%d\t",s[i][j]);
		}
		
	}
	for(i=0;i<4;i++){
		tmp=0;
		
		for(j=0;j<3;j++){
			tmp=tmp+s[i][j];
		}
		t[i]=tmp;
	}
	printf("\n\n PRINT TABLE\n\n");
	for(i=0;i<4;i++){
		printf("%d\t %d\n",i,t[i]);
}
	return 0;		
}
