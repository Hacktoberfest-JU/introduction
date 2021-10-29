#include<iostream.h>
#include<conio.h>
void main()
{
  clrscr();
  int a,b,sum,devide,subtract,multiply;
  cin>>"Enter the first number : ";
  cin>>"Enter the second nummber : ";
  sum = a+b;
  multiply = a*b;
  subtract = a-b;
  devide = a/b;
  cout<<"The sum of the two numbers : "<<sum;
  cout<<"The multplication of the given two numbers is : "<<multiply;
  cout<<"The subtracion of the given two numbers is : "<<subtract;
  cout<<"The devision of thr given two numbers is : "<<devide;
  if (sum%2==0)
  cout<<"The sum of the given two numbers is even :)";
  else
  cout<<"The sum of the given two numbers id odd :(";
  getch()
}
  
