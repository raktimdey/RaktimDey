#include <stdio.h>

int main(){

    int i=0;

    srand(time(NULL));
    while (i<15){

            printf("%d\n",rand()%100);
        i++;
    }

    return 0;
}
