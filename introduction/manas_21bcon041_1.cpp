#include<iostream.h>
#include<conio.h>
void main()
{
  clrscr();
  float SI,P,R,T;
  cout<<"Enter the value of P = ";
  cin>>P;
  cout<<"Enter the value of R = ";
  cin>>R;
  cout<<"Enter the value of T = ";
  cin>>T;
  SI=(P*R*T)/100;
  cout<<"Simple Interest = "<<SI;
  getch();
}
