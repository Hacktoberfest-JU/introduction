Operation=input("Please Enter The Operation(+,-,*,/) You Want To Perform --> ")
num1=int(input("Enter First Number --> "))
num2=int(input("Enter Second Number --> "))
if Operation=='+':
    print("The Sum of Both Numbers is --> ",num1+num2)
elif Operation=='-':
    print("The Subtraction of Both Numbers is --> ",num1-num2)
elif Operation=='*':
    print("The Multiplication of Both Numbers is --> ",num1*num2)
elif Operation=='/':
    print("The Division of Both Numbers is --> ",num1/num2)
else:
    print("Please Enter only +, -, *, /")
