#include <set>
#include <iostream>
using namespace std;
class des_sort
{
public:
  //overloading the operator() function;
    bool operator()(int a, int b)
    {
        return a > b;
    }
};
int main()
{
  //use a class a comperator function;
    multiset<int, des_sort> m;
    m.insert(2);
    m.insert(3);
    m.insert(3);
    m.insert(5);
    m.insert(2);
    m.insert(6);
    for (auto it : m)
        cout << it << " ";
}
