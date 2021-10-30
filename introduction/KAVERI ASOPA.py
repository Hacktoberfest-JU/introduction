# to find the lowest and second lowest integer from 10 integer
small = smaller = 0
for i in range(10):
  n=int(input("Enter The Number:"))
  if i==0:
    small=n
  elif i == 1:
    if n <=small:
      smaller=n
    else:
      smaller=small
      small=n
  else:
    if n <smaller:
      small=smaller
      smaller=n
    elif n<small:
      small=n
  
  print("the lowest number is:",smaller)
  print("the second lowest number is:",small)
    
