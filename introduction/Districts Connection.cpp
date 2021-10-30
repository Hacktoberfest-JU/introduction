#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int n;
    cin >> n;
    int a[n];
    map<int, vector<int>> mp;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        mp[a[i]].pb(i + 1);
    }
    if (mp.size() == 1)
    {
        cout << "NO\n";
        return;
    }
    cout << "YES\n";
    int con = mp.begin()->second[0];
    int flag = 0;
    for (auto it : mp)
    {
        if (flag == 0)
        {
            flag = 1;
        }
        else
        {
            for (auto it1 : it.second)
                cout << con << " " << it1 << endl;
        }
    }
    auto it = mp.begin();
    it++;
    if (it != mp.end())
    {
        con = it->second[0];
        auto it = mp.begin()->second;
        flag = 0;
        for (auto it1 : it)
        {
            if (flag == 0)
                flag = 1;
            else
            {
                cout << con << " " << it1 << endl;
            }
        }
    }
}

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        solve();
        // cout << endl;
    }
}
