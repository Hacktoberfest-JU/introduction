#include<iostream>
using namespace std;

int main()
{
	int p,r,t,i;
		cout << "\n\n Calculate the Simple Interest :\n";
	cout<<" Input the Principle: ";
	cin>>p;
	cout<<" Input the Rate of Interest: ";
	cin>>r;
	cout<<" Input the Time: ";
	cin>>t;
	i=(p*r*t)/100;
	cout<<" The Simple Interest for the amount "<<p<<" for "<<t<<" years @ "<<r<<" % is: "<<i;
	return 0;
}
