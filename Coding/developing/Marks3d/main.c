#include <stdio.h>
#include <stdlib.h>

int main()
{
    int s[3][4][3], t[3][4],tmp;
    int i,j,k;

    for(i=0;i<3;i++){
        for(j=0;j<4;j++){

            printf("Enter part1,2 & 3 marks for students no %d & Subject no %d\n",i,j);
            for(k=0;k<3;k++){
                scanf("%d",&s[i][j][k]);
            }
        }
    }
    //calculation
      for(i=0;i<3;i++){
        for(j=0;j<4;j++){
             tmp=0;
           for(k=0;k<3;k++){
                tmp=tmp+s[i][j][k];
            }
            t[i][j]=tmp;
            }
    }

//print

    printf("Total Marks");
    for(i=0;i<3;i++){
        printf("%d\t",i);
        for(j=0;j<4;j++){
            printf("%d\t",t[i][j]);
        }
        printf("\n");
    }
    return 0;
}
