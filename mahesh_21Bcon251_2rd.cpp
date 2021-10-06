#include<iostream>
using namespace std;
void convetTo(int);
int main()
{
   	int num;
    	cout<<"Enter a number : ";
   	cin>>num;
	cout<<endl;
   	convetTo(num);
}

void convetTo(int value)
{
   	const char * const ones[20] = {"zero", "one", "two", "three","four","five","six","seven",
    	"eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
    	"eighteen","nineteen"};
    	
	const char * const tens[10] = {"", "ten", "twenty", "thirty","forty","fifty","sixty","seventy",
    	"eighty","ninety"};

   	if(value<0)
    	{
		cout<<"minus ";
        	convetTo(-value);
	}
   
	else if(value>=1000)
 	{
        	convetTo(value/1000);
        	cout<<" thousand";

        	if(value % 1000)
        	{
            		if(value % 1000 < 100)
            		{
                		cout << " and";
            		}
            		cout << " " ;
            		convetTo(value % 1000);
        	}
    	}
    
	else if(value >= 100)
    	{
        	convetTo(value / 100);
        	cout<<" hundred";

        	if(value % 100)
        	{
            		cout << " and ";
            		convetTo (value % 100);
        	}
    	}
    
	else if(value >= 20)
    	{
        	cout << tens[value / 10];
        	if(value % 10)
        	{
            		cout << " ";
            		convetTo(value % 10);
        	}
    	}
    
	else
    	{
        	cout<<ones[value];
    	}
    
	return;
}
