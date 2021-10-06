#include<stdio.h>
#include<conio.h>
int main()
{
    int a;
    int b;

    printf("Enter the first value\n");
    scanf("%d", &a);

    printf("Enter the second value\n");
    scanf("%d", &b);

    if (a == b)
    {
        printf("the value of a equals to b\n");
        printf("And the value is %d\n", a);
    }

    else
    {
        printf("The value of a is not equals to b\n");
    }
    return 0;
}
