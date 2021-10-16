#include<iostream.h>
#include<conio.h>
template <class t>
t swap(t &a, t &b)
{
 t c;
 c=a;
 a=b;
 b=c;
}
main()
{
int a,b;
float i,j;
cout<<"enter the value of a,b";
cin>>a>>b;
cout<<"enter the value of i,j";
cin>>i>>j;
swap(a,b);
swap(i,j);
cout<<a<<" "<<b;
cout<<endl;
cout<<i<<" "<<j;
getch();
}
