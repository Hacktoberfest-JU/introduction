// N = 3
// matrix[][] = {{1,2,3},

//               {4,5,6},

//               {7,8,9}}
// Output:
// 1 2 4 3 5 7 6 8 9

vector<int> antiDiagonalPattern(vector<vector<int>> m) 
    {
        vector<int>v;
        int n=m.size();
        for(int k=0;k<n;k++)
        {
            for(int i=0,j=k;j>=0;j--, i++)
            {
                v.push_back(m[i][j]);
            }
        }
        for(int k=1;k<n;k++)
        {
            for(int i=k,j=n-1;j>=0 && i<n; j--,i++)
            {
                v.push_back(m[i][j]);
            }
        }
        return v;
    }
