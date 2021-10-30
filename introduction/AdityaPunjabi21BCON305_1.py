y=int(input("Enter the Year :- "))
x=int(input("Enter the Number of Month you want to know the days of :- "))
if x in (1,3,5,7,8,10,12):
    print("The Month has 31 Days☻☻")
elif x in (4,6,9,11):
    print("The Month has 30 Days☻☻")
elif x==2:
    if y%4==0:
        print("This Month has 29 Days☻☻")
    else:
        print("This Month has 28 Days☻☻")
