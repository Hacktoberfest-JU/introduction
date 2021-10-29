#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    string s1,s2;
    cin>>s1>>s2;
  
    ll n=s1.size();
    ll x=s2.size();
  
    ll c=0,count=0,i,j;
    
    for(i=0;i<=n-x;i++)
    {
        if(s1.substr(i,x)==s2)
        {
            count++;
            i=i+x-1;
        }
    }
    cout<<count<<endl;
}
