Choice (In C)
#include<stdio.h>

int main()
{
int choice,a,b,c;
printf("\n1. Addition");
printf("\n2. Odd-Even");
printf("\n3. Printing N numbers");

printf("\nEnter your Choice");
scanf("%d",&choice);
switch(choice)
{
case 1:
printf("Enter the number");
scanf("%d%d",&a,&b);
c=a+b;
printf("Sum is %d",c);

break;

case 2:
printf("Enter the number");
scanf("%d",&a);
if(a%2==1)
printf("Odd");
else
printf("Even");
break;
case 3:
printf("Enter the number");
scanf("%d",&a);
for(b=1;b<=a;b++)
printf("%d",b);
break;
default:
printf("invalid number");
}
return 0;
}
