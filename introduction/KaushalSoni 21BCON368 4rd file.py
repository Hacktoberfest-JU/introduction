# This program is used to identify the profit and loss on the particular item
n=int(input("Enter no. of Items:"))
t=0
S=0
K=0
for i in range (0,n):
    c=int(input("Enter Cost Price of Item:"))
    s=int(input("Enter Selling Price of Item:"))
    t+=c
    S+=s
print ('Total Cost Price is:',t)
print ('Total Selling Price is:',S)
if S>t:
    p=S-t
    K=p
    print('profit is:')
else:
    l=t-S
    K=l
    print('Loss is:')
print(K)
