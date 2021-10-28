#include<iostream>
using namespace std;
int main()
{ 
float SI,P, R;
int T;
cout<<"Enter Principal Amount:- ";
cin>>P;
cout<<"Enter Time:- ";
cin>>T;
cout<<"Enter Rate of Interest:- ";
cin>>R;
SI=(P*T*R)/100;
cout<<"Simple Interest is "<<SI;
}
