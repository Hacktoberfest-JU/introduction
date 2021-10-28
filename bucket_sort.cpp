// #include <iostream>
// #include <vector>
// #include <algorithm>
#include <bits/stdc++.h>
#define fast_io ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
using namespace std;

class student {

public:
    int marks;
    string name;

};

//Bucket sort to sort an array of students
void bucket_sort(student s[], int n) {

    // assuming marks are in range 0-100
    vector<student> v[101];

    //O(n) time
    for (int i = 0; i < n; i++) {
        int m = s[i].marks;
        v[m].push_back(s[i]);
    }

    // iterate over the vector and print elements

    for (int i = 100; i >= 0; i--) {

        for (vector<student>::iterator it = v[i].begin(); it != v[i].end(); it++) {
            cout << (*it).marks << " " << (*it).name << endl;
        }

    }

}

int main()
{

    fast_io;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("error.txt", "w", stderr);
    freopen("output.txt", "w", stdout);
#endif

    student s[100000];
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> s[i].marks >> s[i].name;
    }
    bucket_sort(s, n);

    return 0;
}
