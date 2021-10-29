#include<iostream>
using namespace std;

int main(){

    char button;
    cout<<"input a character"<<endl;
    cin>>button;

    switch(button){

    case'a':
    cout<<"hello"<<endl;
    break;

    case'b':
    cout <<"namastee" << endl;
    break;

    case'c':
    cout <<"ciao"<< endl;
    break;

    case'd':
    cout <<"hello ji"<< endl;
    break;

    case'e':
    cout<<"sastriyakal"<<endl;
    break;

    default:
    cout<<" Not Available"<<endl;

    }
    return 0;
}

