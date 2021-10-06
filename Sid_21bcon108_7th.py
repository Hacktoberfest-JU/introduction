def chknos(a, b):
    if a>b:
        print("the first number ",a,"is greater")
        return a
    else:
        print("the second number ",b,"is greater")
        return b        

import greatfunc
a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
ans=greatfunc.chknos(a, b)
print("GREATEST NUMBER = ",ans)
