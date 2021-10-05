#include<stdio.h>
#include<conio.h>
void main()
{
  int r,n,j,s,p,a,b,c,t,d;
  printf("Enter the number")
    scanf("%d",&n);
  t=n;
  s=n*n;
  a=0;b=0;c=0;p=1;
  while(n>0)
  {
    j=s%10;
    r=n%10;
    if(j==r&&p==1)
    a=j;
    else if (j==r&&p==2)
      b=j;
    else if (j==r&&p==3)
      c=j;
    n=n/10;
    s=s/10;
    p++;
  }
  d=c*100+b*10+a;
  if(d==t)
    printf("yes");
    else
      printf("no");
  getch();
}
