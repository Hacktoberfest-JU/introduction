x=int(input("Number of terms:- "))
num=0
num2=1
count=0
if x<=0:
    print("Enter a positive integer.")
elif x==1:
    print("fibonacci series upto ",x)
    print(num)
else:
    print("Fibonacci sequence:- ")
    while count < x:
        print(num)
        nth=num+num2
        num=num2
        num2=nth
        count+=1
