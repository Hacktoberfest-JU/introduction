#include <bits/stdc++.h>
#define QUICK ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
using namespace std;
void solve()
{
    int n, e, a, b;
    cin >> n >> e;
    map<int, set<int>> mp;
    for (int i = 0; i < e; i++)
    {
        cin >> a >> b;
        mp[a].insert(b);
        mp[b].insert(a);
    }
    int flag = 1, cnt = 0;
    while (flag == 1)
    {

        flag = 0;
        vector<int> v;
        for (auto it : mp)
        {
            if (it.second.size() == 1)
            {
                flag = 1;
                v.pb(it.first);
            }
        }

        for (auto it : v)
        {
            for (auto it1 = mp.begin(); it1 != mp.end(); it1++)
            {
                if (it1->second.find(it) != it1->second.end())
                {
                    it1->second.erase(it);
                }
            }
        }

        for (auto it : v)
            mp.erase(it);
        if (flag == 1)
            cnt++;
    }
    cout << cnt << endl;
}

int main()
{
    QUICK;
    // string s;
    // ll arr[si];
    // sieve(arr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    // w(t)
    {
        solve();
        // cout << endl;
    }
}
