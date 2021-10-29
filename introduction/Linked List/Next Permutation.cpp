#include <bits/stdc++.h>
using namespace std;
void permute(string a, int l, int r, vector<string> &v)
{
    if (l == r)
        v.push_back(a);
    else
    {
        for (int i = l; i <= r; i++)
        {
            swap(a[l], a[i]);
            permute(a, l + 1, r, v);
            swap(a[l], a[i]);
        }
    }
}
int main()
{
    string str, a;
    cin >> str;
    a = str;
    for (int i = 0; i < 8; i++)
    {
        next_permutation(str.begin(), str.end());
        cout << str << " ";
    }
    vector<string> v;
    cout << endl
         << endl;
    permute(a, 0, str.size() - 1, v);
    sort(v.begin(), v.end());
    for (auto it : v)
        cout << it << endl;
}
