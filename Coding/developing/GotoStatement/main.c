#include <stdio.h>



int main(){
int i,s;
char a;
s=0;

for(;;)
{
    printf("Enter a number to add:\n");
    scanf("%d",&i);
    s=s+i;
    printf("this is the number:\n",s);
    printf("for exit press E:");
    if(getchar()=='E'){
        break;
    }
    printf("%d",s);
    return 0 ;
}

}
