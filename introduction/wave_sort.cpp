#include <iostream>
#define fast_io ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
using namespace std;

void wave_sort(int *a, int n) {

    for (int i = 0; i < n; i += 2) {

        //Prev element
        if (i != 0 and a[i] < a[i - 1]) {
            swap(a[i], a[i - 1]);
        }
        //next element
        if (i != n - 1 and a[i] < a[i + 1]) {
            swap(a[i], a[i  + 1]);
        }

    }

}


int main()
{
    fast_io;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    // use to sort an array of 0's 1's and 2's.
    int arr[] = {1, 3, 4, 2, 7, 8};
    int n = sizeof(arr) / sizeof(int);
    wave_sort(arr, n);

    for (int i = 0; i < n; ++i)
    {
        cout << arr[i] << " ";
    }

    return 0;
}
