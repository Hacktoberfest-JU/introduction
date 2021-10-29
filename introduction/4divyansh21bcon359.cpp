#include<iostream.h>
#include<conio.h>
void main()
{
  clrscr();
  float c,k,f;
  cout<<"Enter temperature in celcius";
  cin>>c;
  k=273.15+c;
  f=(c*9.0)/5.0 +32;
  cout<<"the temperature in kelvin is "<<k<<endl;
  cout<<"The temperature in farenhite is "<<f<<endl;
  getch();
}
