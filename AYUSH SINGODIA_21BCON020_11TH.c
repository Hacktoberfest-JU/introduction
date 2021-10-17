#include<stdio.h>
#include<string.h>
#include<conio.h>
/* calculate the marks of 5 subjects using for loops and calculate the division of a 
student by his marks using  if else control statement*/

//AND FIND THE PERCENTAGE OF THE GIVEN MARKS //
int main(){

int a,i,percentage;
int marks[15];
int sum=0;
int totalmarks=500;
char name[30];


puts("Enter the name of a student\n");
scanf("%s",name);

fputs("student name :" ,stdout);
puts(name);

printf("Enter the marks of 5 students\n");
for(i=0; i< 5; i++)
scanf("%d" ,&marks[i]);

for(i=0; i<5; i++ )
sum=sum+marks[i];


percentage = (float)sum/ totalmarks * 100.0;






printf("you got %d total marks\n" ,sum);

if (sum>390)
{
   printf("CONRATS YOU GOT FIRST DIVISION\n");
   printf("MARKS IN PERCANTAGE :%d\n" ,percentage);

}
else
{
    printf("CONGRATS YOU GOT SECOND DIVISION \n");
    printf("MARKS IN PERCANTAGE :%d\n" ,percentage);
}


    return 0;
}
