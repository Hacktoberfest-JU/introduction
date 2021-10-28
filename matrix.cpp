#include<iostream.h>
#include<conio.h>
void main()
{
int a[3][3], b[3][3], c[3][3];
char ch, a;
cout<<"Enter the elements of 1st array";
for(int i=0; i<3; i++)
{
for(int j=0; j<3; j++)
{
cin>>a[i][j];
}
}
cout<<"Enter the elements of the 2nd array";
for(i=0; i<3; i++)
{
for(j=0; j<3; j++)
{
cin>>b[i][j];
}
}
cout<<"Press 1 if you want to add the two matrices"<<endl;
cout<<"Press 2 if you want to subtract the two matrices"<<endl;
cout<<"Press 3 if you want to find the transpose of any of the two matrices"<<endl;
cout<<"Enter your choice";
cin>>ch;
switch(ch)
{
case 1:
for(i=0; i<3; i++)
{
for(j=0; j<3; j++)
{
c[i][j]=a[i][j]+b[i][j];
}
}
Cout<<"The sum of the given two matrices is";
for(i=0; i<3; i++)
{
for(j=0; j<3; j++)
{
cout<<c[i][j];
}
}
break;
case 2:
for(i=0; i<3; i++)
{
for(j=0; j<3; j++)
{
c[i][j]=a[i][j]-b[i][j];
}
}
Cout<<"The subtraction of the given two matrices is";
for(i=0; i<3; i++)
{
for(j=0; j<3; j++)
{
cout<<c[i][j];
}
}
break;
case 3:
cout<<"Enter the array whose tranpose you want to find";
cin>>x;
if(x=='a')
{
Cout<<"The transpose of the given matrix is";
for(i=0; i<3; i++)
{
for(j=0; j<3; j++)
{
cout<<a[j][i];
}
}
}
else if(x=='b')
{
Cout<<"The transpose of the given matrix is";
for(i=0; i<3; i++)
{
for(j=0; j<3; j++)
{
cout<<b[j][i];
}
}
}
else
{
cout<<"Invalid input";
}
break;
Default:
Cout<<"The entered input is invalid";
break;
}
getch();
}
