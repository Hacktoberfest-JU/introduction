//THIS CODE IS WRITTEN BY  AYUSH SINGODIA
#include<stdio.h>

int main()
{
    char operator;
     int a , b ,sum , sub , division ,multipication;
 printf("enter an operator (+, -, *, /,)\n");
 scanf("%c" ,&operator);
 printf("enter two operands \n");
 scanf("%d %d" ,&a ,&b);


 switch(operator)
 {
     case '+':
     sum=a+b;
     printf("sum is equals =%d \n" ,sum);
     break;

     case'-':
     sub=a-b;
     printf("sub is equals to =%d \n" ,sub);
     break;

     case'*':
     multipication=a*b;
     printf("multipication=%d \n" ,multipication);
     break;

     case'/':
     division=a/b;
     printf("division=%d\n" ,division);
     break;
     
     

     

     default :printf("not found\n");
 }
 return 0;
}
