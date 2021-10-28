#include <iostream>
#include <string>
using namespace std;
int is_pallindrome(string s)
{
    int i = 0, j = s.size() - 1;
    while (i <= j)
    {
        if (s[i] != s[j])
            return 0;
        i++;
        j--;
    }
    return 1;
}
void solution(string str, string res_so_far)
{
    if (str.size() == 0)
    {
        cout << res_so_far << endl;
        return;
    }
    for (int i = 0; i < str.size(); i++)
    {
        string prefix = str.substr(0, i + 1);
        string remaining_str = str.substr(i + 1);
        if (is_pallindrome(prefix))
            solution(remaining_str, res_so_far + prefix + " ");
    }
}
int main()
{
    string s, rest_of_string, string_res = "";
    cin >> s;
    rest_of_string = s;
    solution(rest_of_string, "");
}
