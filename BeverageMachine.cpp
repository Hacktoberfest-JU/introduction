#include <iostream>
using namespace std;
int main()
{

    cout << "what would u like to drink\n For Capachino coffee press A\n For tea press B\n For water press C\n For Green Tea press D\n";
    char button;
    cin >> button;

    switch (button)
    {

    case 'A':
        cout << "Your coffee is preparing" << endl;
        break;

    case 'B':
        cout << "Your tea is being prepared" << endl;
        break;

    case 'C':
        cout << "Take your water" << endl;
        break;

    case 'D':
        cout << "Your Green tea is ready" << endl;
        break;

    default:
        cout << "invalid option" << endl;
    }
    return 0;
}
