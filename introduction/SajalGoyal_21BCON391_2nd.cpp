#include <iostream>
using namespace std;

int main()
{
    int age;
    cout<<"Enter Your Age:";
    cin>>age;
    if (age>150)
    {
        cout<<"Invalid Age";
    }
    else if (age>=18)
    {
        cout<<"You are Eligible To Vote";
    }
    
    else
    {
        cout<<"You are not eligible to vote";

    }
    return 0;
}
