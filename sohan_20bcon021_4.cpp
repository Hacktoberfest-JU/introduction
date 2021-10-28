#include<iostream.h>
#include<conio.h>
#include<fstream.h>
class emp
{
int age,sal;
char name[20],city[20];
public:
void insert ()
{
cout<<"enter the details";
cin>>name>>city>>age>>sal;
}
void show ()
{
cout<<name<<city<<age<<sal;
}
};
main()
{
emp e;
ofstream fout;
char ch;
fout.open("Sohan Beniwal.txt",ios::binary|ios::out);
while(1)
{
e.insert();
fout.write((char*)&e,sizeof(e));
cout<<"do you want add more";
cin>>ch;
if(ch=='n')
break;
}
fout.close();
getch();
}
