#include<iostream.h>
#include<conio.h>
void main()
{
  clrscr();
  float a,b,c;
  cout<<"Enter three numbers that you want to compare";
  cin>>a>>b>>c;
  if ((a>=b) && (a>=c));
  {
    cout<<"the greatest number is : "<<a;
  }
  else if ((b>=a) && (b>=c))
  {
    cout<<"the greatest number is : "<<b;
  }
  else
  {
    cout<<"the greatest number is : "<<c;
  }
  getch();
}
