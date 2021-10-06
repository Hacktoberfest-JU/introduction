num1=int(input("Enter Number :- "))
factorial=1
if num1<0:
    print("Enter A Positive Number")
elif num1==0:
    print("Factorial of 0 is 1.")
else:
    while (num1>0):
        factorial=factorial*num1
        num1-=1
print("Factorial is",factorial)
