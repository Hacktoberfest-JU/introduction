#include <iostream>
using namespace std;

int main()
{
int n, s=0, r, a;
cout<<"Enter the number";
cin>>n;
a=n;
while (a>0)
{
    r=a%10;
    s=s*10+r;
    a=a/10;
}
if (s==n)
{
    cout<<s<<" is a palindrome";
}
else
{
cout<<s<<" is not a palindrome";
}
return 0;
}
