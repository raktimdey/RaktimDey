#include <stdio.h>

int main(){

int i, prime=0,rd=0,num=0;

printf("Enter any Number:\n");
scanf("%d",&num);

for(i=2;i<=num;i++){
    rd=i%num;
    if(rd==0){
        prime=1;
        break;
    }
}
if(prime==0){
    printf("%d is a prime number.",num);
}
else{
    printf("%d is not a prime number",num);
}
return 0;
}
