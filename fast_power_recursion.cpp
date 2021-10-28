#include <bits/stdc++.h>
#define fast_io ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
using namespace std;
int power(int a, int n) {
    if (n == 0)                 //O(n)
        return 1;
    return a * power(a, n - 1);
}
int fast_power(int a, int n) {
    if (n == 0)
        return 1;               //O(log(n))
    //rec case
    int small_ans = fast_power(a, n / 2);
    small_ans *= small_ans;

    if (n & 1)
        return small_ans * a;
    else
        return small_ans;
}


int main()
{
    fast_io;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int a, n;
    cin >> a >> n;
    cout << power(a, n) << endl;
    cout << fast_power(a, n) << endl;


}
