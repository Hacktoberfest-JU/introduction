/*
Name: Shikha Pandya
Roll no: 21BCON049
Program: Lift
Description: Working of lift implimented in c++ with a cool user interface
*/
#include<iostream>
#include<string.h>
#include<conio.h>
#include<unistd.h>
using namespace std;
int main()
{
	char p[10];
	strcpy(p,"L        ");
	int loop=0;
	int u,lf=0,b,t;
	cout/*<<"-------------------------|"*/<<endl<<endl;
	cout<<" Lift is on "<<u<<" floor..."<<endl;
	cout<<" 0 1 2 3 4 5 6 7 8 9 "<<endl;
	cout<<" ^"<<endl;

while(loop==0) {	
	cout<<" Where are you: ";
	cin>>u;
	cout<<endl<<"Please wait lift is processing..."<<endl;
	cout<<"-------------------------|"<<endl;
    sleep(1);
	while(u!=lf)
	{
	

	if(u<lf) {p[lf]=' '; lf--;	p[lf]='L'; }	
	else {p[lf]=' '; lf++; p[lf]='L';	}
    cout<<"-------------------------|"<<endl;

	for(b=9;b>=0;b--)
	{
		//cout<<"-------------------------|"<<endl;
		cout<<b<<p[b]<<"                       |"<<endl;
		cout<<"-------------------------|"<<endl;
	}
	cout<<endl<<endl<<endl<<endl<<endl;
		sleep(2);		
	}
	
	
	cout<<"Please be in the lift..."<<endl<<endl;
	cout<<"Where do you want to go: ";
	cin>>u;
	cout<<"-------------------------|"<<endl;
	
	while(u!=lf)
	{

	if(u<lf) {p[lf]=' '; lf--;	p[lf]='L'; }	
	else {p[lf]=' '; lf++; p[lf]='L';	}
	cout<<"-------------------------|"<<endl;

	for(b=9;b>=0;b--)
	{
		//cout<<"-------------------------|"<<endl;
		cout<<b<<p[b]<<"                       |"<<endl;
		cout<<"-------------------------|"<<endl;
	}
	cout<<endl<<endl<<endl<<endl<<endl<<endl;
		sleep(3);
	}
		
	cout<<"      You have reached your destination..."<<endl;
	cout<<"|****--------------------------------------****|"<<endl;
}
}
