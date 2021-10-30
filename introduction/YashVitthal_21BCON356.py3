def recurfactorial(n);
     if n==1:
          return n
     else:
          retun n*recurfactorial(n-1)
num=int(input("Enter a number:"))
if num<0:
     print("Sorry,No factorial for negative numbers")
elseif num==0:
     print("The factorial of 0 is 1")
else:
     print("The factorial of",num,"is",recurfactorial(num))
          
