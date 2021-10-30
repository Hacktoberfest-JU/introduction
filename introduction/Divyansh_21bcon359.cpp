#include<iostream.h>
#include<conio.h>
void main()
{
  clrscr();
  int a,b,c:
  cout<<"Enter three numbers";
  cin>>a>>b>>c;
  if (a>b&&a>c)
    cout<<a<<"is greatest";
  else if (b>a&&b>c)
    cout<<b<<"is greatest";
  else
    cout<<c<<"is greatest";
  getch();
}
