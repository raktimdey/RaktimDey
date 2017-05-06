#include<stdio.h>

int main(){
	
	int s[3][4][3],t[3][4],tmp,i,j,k;
	
	for(i=0;i<3;i++){
		for(j=0;j<4;j++){
			printf("Enter marks for Student no%d &Subject no%d",i,j);
			for(k=0;k<3;k++){
				scanf("%d",&s[i][j][k]);
			}
		}
	}
	
		
	for(i=0;i<3;i++){
		for(j=0;j<4;j++){
			tmp=0;
			for(k=0;k<3;k++){
				tmp=tmp+s[i][j][k];
			}
		}
	}
	printf("\n\n TOTAL MARKS \n\n");
		
	for(i=0;i<3;i++){
		printf("%d\t",i);
		for(j=0;j<4;j++){
			printf("%d\t",t[i][j]);
			
			}
		}
	}

