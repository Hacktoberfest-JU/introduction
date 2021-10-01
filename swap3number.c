#include<stdio.h>
int main(){
int a,b,c,t;
printf("enter 3 integer number:");
scanf("%d%d%d",&a,&b,&c);
t=a;
a=b;
b=c;
c=t;
printf("after swap value is %d,%d and %d"a,b,c);
return(0);
}
