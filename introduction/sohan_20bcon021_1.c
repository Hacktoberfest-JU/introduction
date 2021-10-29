#include<stdio.h>
#include<conio.h>
void main ()
{
  char a[10];
  int i,j;
  printf("Enter the name to check pallindrome");
  scanf("%s",a);
  for(i=0;a[i]!=NULL;i++);
  j=i-1;
  for(i=0;i!=j;i++,j--)
  {
    if(a[i]!=a[j])
      break;
  }
  if(a[i]==a[j])
    printf("Name is pallindrome");
  else
    printf("Name is not pallindrome");
  getch();
}

    
