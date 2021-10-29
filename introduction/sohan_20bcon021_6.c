#include<stdio.h>
#include<conio.h>
void main()
{
int i;
for(i=1;i<=73;i++)
{
clrscr();
gotoxy(80-i,12);
printf("L");
delay(100);
}
for(i=1;i<=72;i++)
{
clrscr();
gotoxy(80-i,12);
printf("o");
printf(" ");
delay(100);
}
for(i=1;i<=71;i++)
{
clrscr();
gotoxy(80-i,12);
printf("a");
printf(" ");
delay(100);
}
for(i=1;i<=70;i++)
{
clrscr();
gotoxy(80-i,12);
printf("d");
printf(" ");
delay(100);
}
for(i=1;i<=69;i++)
{
clrscr();
gotoxy(80-i,12);
printf("i");
printf(" ");
delay(100);
}
for(i=1;i<=68;i++)
{
clrscr();
gotoxy(80-i,12);
printf("n");
printf(" ");
delay(100);
}
for(i=1;i<=67;i++)
{
clrscr();
gotoxy(80-i,12);
printf("g");
printf(" ");
delay(100);
}
getch();
}
