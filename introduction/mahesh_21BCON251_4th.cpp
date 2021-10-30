#include<iostream>
using namespace std;

int main()
{

    //declaration of variables
    int num1, num2, num3;
    int smallest, largest;

    //take input from user
    cout << "Please enter 3 numbers : "<<"" ;
    cin >> num1 >> num2 >> num3;

    //assign initial value for comparison
    smallest = num1;
    largest = num1;

    if (num2 > largest)
        {
           largest = num2;
        }

    if (num3 > largest)
        {
            largest = num3;
        }

    if (num2 < smallest)
        {
            smallest = num2;
        }

    if (num3 < smallest)
        {
            smallest = num3;
        }

        //display largest number and smallest number
    cout << "largest: " << largest << "\nsmallest: " << smallest << "\n";
}
