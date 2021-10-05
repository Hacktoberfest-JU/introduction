#Armstrong Number
import numpy as np
x=list(np.arange(1000))
a=[]
for i in x:
    store=i
    b=0
    while i!=0:
        c=i%10
        b=b+c**3
        i=i//10
    if b==store:
        a.append(b)
print('no. is armstrong')
for k in range(len(a)):
    print(a[k])
