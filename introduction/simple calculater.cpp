#include<iostream>
using namespace std;

//making a simple calculater

int main(){
    
     float n1,n2;
     cout<<"input 2 num"<<endl;
     cin>>n1>>n2;

     char op;
     cout<<"input a operator"<<endl;
     cin>>op;

     switch(op){
         case '+':
        cout << n1+n2 <<endl;
        break;

      case '-':
      cout << n1-n2 <<endl;
      break;

      case '/':
      cout << n1/n2 <<endl;
      break;

      case '*':
      cout  << n1*n2 <<endl;
      break;

      default:
      cout <<"choose another operatorr" <<endl;
    break;
}
     return 0;


}
