#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
char ch;
int a;
cout<<"Enter money in Rupees";
cin>>a
cout<<"Enter D if you want to convert into Dollar"<<endl;
cout<<"Enter E if you want to convert into Euros"<<endl;
cout<<"Enter W if you want to convert into Won"<<endl;
cout<<"Enter Y if you want to convert into Yen"<<endl;
cout<<"Enter C if you want to convert into chinese Yuan"<<endl;
cout<<"Enter your choice";
cin>>ch;
switch(ch)
{
case 'D':
cout<<"The given amount of Rupess in Dollar would be="<<a*0.013;
break;
case 'E':
cout<<"The given amount of Rupess in Euros would be="<<a*0.012;
break;
case 'W':
cout<<"The given amount of Rupess in Won would be="<<a/15.68;
break;
case 'Y':
cout<<"The given amount of Rupess in Yen would be="<<a*1.52;
break;
case 'C':
cout<<"The given amount of Rupess in chinese Yuan would be="<<a*0.085;
break;
}
getch();
}
