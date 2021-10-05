#include <iostream>
using namespace std;

int main() {
    int num;
    
    cout << "Enter an integer: ";  
     cin >> num;

    if (num != 0) {

        if ((num % 2) == 0) {
            
            cout << "The number is even." << endl;
        }
        else {
            cout << "The number is odd." << endl;
        }  
    }
    else {
        cout << "The number is 0 and it is neither even nor odd." << endl;
    }
    
}
