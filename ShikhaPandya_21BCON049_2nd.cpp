#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void wait(int seconds);
void welcome_screen();
void bill(float billmoney);
int penceentered();
int menu(); 
int differentcoins();
void Gachatotal(int selection,int amount);
void Pokemonchosen(int selection);
float cost(int selection);

int main()
{
	welcome_screen();
	
	int q;
	int entered;
	int amount;
	int cancle;
	int select;
	int selection;
	int pence;
	int billreq;
	int change;
	float Pokemax;
	float billmoney;
	float itemprice;
	float coinselected;
	float total;
	
	selection = menu();
	Pokemonchosen(selection);
	
	if(selection>0 && selection<5)
	{
		printf("\n\n  Press 1 to continue or 2 to cancle the order.\n  ");
		scanf("%d",&cancle);
		
		if(cancle==1)
		{
			printf("  How much? (Max 5)\n  ");
			scanf("%d",&amount);
			if(amount<=5)
			{
				itemprice = cost(selection);
				Pokemax = amount*itemprice;
				bill(Pokemax);
				x:pence=penceentered();
				
				if(pence==100 || pence==150 || pence==200 || pence==300 ||pence==500)
				{
					while(total<=Pokemax)
					{
						total=total+pence;
						billreq=Pokemax-total;
						
						if(total<Pokemax)
						{
							printf("\n\n  Your outstanding money is %d p",billreq);
							printf("\n\n");
							goto x;
						}
						
						else if(total>Pokemax)
						{
							change=total-Pokemax;
							Gachatotal(selection,amount);
							
							for(q=1;q<=amount;q++)
							{
								printf("\t\t\tPokeBall #%d is being dispensed\n",q);     //PokeBall Or PokeType
								wait(3);
				            }
				            printf("\n\t\t  Your change is %dYen \n\n",change);
				            printf("\n\t\t   ***Thank You And Hope You'll Catch Some More Pokemons!!***");
				            break;
						}
						else
						{
							Gachatotal(selection,amount);
							for(q=1;q<=amount;q++)
							{
								printf("\t\t\tPokeBall #%d is being dispensed\n",q);
								wait(5);
				            }
				            printf("\n\t\t   ***Thank You And Hope You'll Catch Some More Pokemons!!***");
				            break;
						}
					}
				}
				else
				{
					printf("\n  Money not acceptable! Please try again\n\n");
					goto x;
				}
				
			}
			else
			{
				printf("  Maximum quantity is 5. Please try again\n");
				menu();
			}
		}
		else
		{
			printf("  Your order has been cancelled\n\n");
			menu();
		}
	}
	else
	{
		printf("  Your order has been cancelled\n\n");
		menu();
	}
}

void welcome_screen()
{
	printf("\t\t (*^.^*) (^.^) Welcome to our Japanese Gacha Machine!! (*^.^*) (^.^)\n\n");
	printf("\t\t\t\t\t\tKonichiwa \n\t\t\t\twelcome to Pokemon Vending Machine!!!\n\n\n");
	//printf("(\_/)\n(•w•)\n/u u\\n|   |\n\ww/\n");
	
	return;
}

void bill(float billmoney)
{
	printf("  Total amount to be payed is : %2f\n\n\n",billmoney);
	return;
}

int penceentered()
{
	int pence;
	printf("  Enter your money: \n");
	printf("  (Y100 Y150 Y200 Y300 Y500)\n  ");
	//printf("\t\t\t***Thank You And Hope You'll Catch Some More Pokemons!!***\t\n\n");
	scanf("%d",&pence);
	return pence;
}

int menu()
{
	int selection;
	
	printf("\t____________________________________\n");
	printf("\tUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU");
	printf("\t\n\t T\t\t\t\t T\n");
	//printf("\tT\n\t|\n");
	printf("\t |-------------------------------|  \n");
	
	printf("\t |LIST :");
	printf("\t\t\t |\n\t |\t\t\t\t |\n");
	printf("\t |1. Charmander");               printf("\t\t Y.89.00 |\n");
	printf("\t |2. Squirtle");               printf("\t\t Y.69.00 |\n");
	printf("\t |3. Bulbasaur");               printf("\t\t Y.49.00 |\n");
	printf("\t |4. Pikachu");              printf("\t\t Y.99.00 |\n");
	printf("\t |5. Quit");
	printf("\t\t\t |\n\t |\t\t\t\t |\n");
	printf("\t |-------------------------------|  \n");
	
	printf("  Please enter your selection : ");
	scanf("%d",&selection);
	
	return selection;    
}

void Pokemonchosen(int selection)
{
	switch(selection)
	{
		case 1:
			printf("  You have selected Charmander.");          printf("\t\t\tY.89.00\n");
			break;
	    case 2:
			printf("  You have selected Squirtle.");          printf("\t\t\tY.69.00\n");
			break;
		case 3:
			printf("  You have selected Bulbasaur.");          printf("\t\t\tY.49.00\n");
			break;
		case 4:
			printf("  You have selected Pikachu.");          printf("\t\t\tY.99.00\n");
			break;
		case 5:
			break;
		default:
		    printf("  Invalid Input!\n");	
		    break;
	}
return;
}

float cost(int selection)
{
	float price=0;
	
	switch(selection)
	{
	case 1:
		price=89.00;
		break;
	case 2:
		price=69.00;
		break;
	case 3:
		price=49.00;
		break;
	case 4:
		price=99.00;
		break;	
	}
	return price;
}

void wait(int seconds)
{
	clock_t end_wait=(clock() + (seconds * CLOCKS_PER_SEC));
	while(clock()<end_wait)
	{}
}

void Gachatotal(int selection, int amount)
{
	switch(selection)
	{
		case 1:
			printf("\n\n\t\t\tYou have selected %d Charmander...\n",amount);
			printf("\t\t\t------------------------------\n");
			break;
		case 2:
			printf("\n\n\t\t\tYou have selected %d Squirtle...\n",amount);
			printf("\t\t\t------------------------------\n");
			break;
		case 3:
			printf("\n\n\t\t\tYou have selected %d Balbasaur...\n",amount);
			printf("\t\t\t------------------------------\n");
			break;
		case 4:
			printf("\n\n\t\t\tYou have selected %d Pikachu...\n",amount);
			printf("\t\t\t------------------------------\n");
			break;
		default:
			printf("Invalid input!!\n");
			break;
	}
}
