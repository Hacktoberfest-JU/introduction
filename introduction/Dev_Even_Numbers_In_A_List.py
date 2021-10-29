# Python Program to Print Even Numbers in a List

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nEven Numbers in this List are : ")
for j in range(Number):
    if(NumList[j] % 2 == 0):
        print(NumList[j], end = '   ')
