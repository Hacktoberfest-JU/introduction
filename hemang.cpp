#include<iostream.h>
int main()
{
  int i,n,f=1;
  std::cout<<"Enter a number ";
  std::cin>>n;
  for(i=n;i>=1;i--)
  {
  f=f*i;}
  std::cout<<"the factorial for the number is "<<f;
return 0;
    
}
