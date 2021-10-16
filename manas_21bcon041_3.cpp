#include<iostream.h>
#include<conio.h>
void main()
{
  clrscr();
  int a=5,b=10;
  cout<<"Before Swapping"<<endl;
  cout<<"a="<<a<<",b="<<b<<endl;
  a=a+b;
  b=a-b;
  a=a-b;
  cout<<"\nAfter Swapping"<<endl;
  cout<<"a="<<a<<",b="<<b<<endl;
  getch();
}
