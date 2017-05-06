#include <stdio.h>
#include <stdlib.h>

int main()
{
   char str[40]="this is a text.";
   FILE *fp;
   char *p;
   int i;
   //open files for iinput
   if((fp=fopen("myfile.txt","w"))==NULL){
    printf("Error opening file.\n");
    exit(1);
   }
   //write str to disk
   p=str;
   while(*p){
    if(fputc(*p,fp)==EOF){
        printf("Error Writing a file.");
        exit(1);
    }
    p++;
   }
   fclose(fp);
   //open again
   if((fp=fopen("myfile.txt","r"))==NULL){
    printf("Error opening a file.");
    exit(1);
   }
   //read back the file
   for(;;){
    i=fgetc(fp);
    if(i==EOF)
        break;
    putchar(i);
   }
   fclose(fp);
    return 0;
}
