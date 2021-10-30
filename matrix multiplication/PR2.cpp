#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
int a[3][3], b[3][3], c[3][3], i, j, sum=0;
cout<<"Enter the elements of matrix 1";
for(i=0;i<3;i++)
{
for(j=0;j<3;j++)
{
cin>>a[i][j];
}
}
cout<<"Enter the elements of matrix 2";
for(i=0;i<3;i++)
{
for(j=0;j<3;j++)
{
cin>>b[i][j];
}
}
for(int row=0;row<3;row++)
{
for(int col=0;col<3;col++)
{
for(i=0;i<3;i++)
{
sum+=a[row][i]*b[i][col];
}
c[row][col]=sum;
}
}
cout<<"The new matrix obtained after multiplication of 1 and 2 is=";
for(i=0;i<3;i++)
{
for(j=0;j<3;j++)
{
cout<<c[i][j]<<" ";
}
cout<<endl;
}
getch();
}
