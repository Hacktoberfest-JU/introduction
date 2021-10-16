#Palindrome Numbers
import numpy as np
x=list(np.arange(101))
a=[]
for i in x:
    store=i
    b=0
    while i!=0:
        c=i%10
        b=b*10+c
        i=i//10
    if b==store:
        a.append(b)
print('Palindrome Numbers Between 1 and 100 are:-')
for k in range(len(a)):
    print(a[k])
