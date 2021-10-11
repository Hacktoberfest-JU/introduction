#include<iostream>
using namespace std;

int main()
{
    int P;
    int R;
    int T;
    cout<<"The Value of P is:";         //It asks the value of Principal.
    cin>>P;
    cout<<"The ValUe of R is:";        //It asks the rate at which the interest is applied.
    cin>>R;
    cout<<"The Value of T is:";         //It asks the time for which the Principal amount is borrowed.
    cin>>T;
    cout<<"The Value of SI for the given conditions is:"<<P*R*T/100;
    return 0;
}
