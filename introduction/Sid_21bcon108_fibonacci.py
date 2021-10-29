def fibonacci(n):
  if n==1:
    return(0)
  elif n==2:
    return(1)
  else:
    return(fibonacci(n-1)+fibonacci(n-2))
  #main
limit=int(input("enter the ending number"))
print("the numbers in the sequence are")
for i in range(1,limit+1):
          print(fibonacci(i))
