# This program is used for generating Bill for n number of items

import datetime

now=datetime.datetime.now()

dtm=str(now)

n=int(input('Enter Total Number of Items:'))

a =0

dict={}

for i in range(1,n+1,1):

    item=input('Enter Name of Item :')

    price=float(input('Enter Price of Item :'))

    qty=int(input('Enter Quantity Required :'))

    val = price * qty

    a += val

    dict[item]=price,qty,val

    tax= a*0.05

    net =a+tax

    i=1

print(dict)

print('-'*65)

print('\t\t\t\tINVOICE')

print('-'*65)

print()

print('date:{0:>55s}'.format(dtm))

print('-'*65)

print('ITEM\t\t\tUnit Price\tQuantity\tValue')

print('-'*65)

for k,v in dict.items():

    print('{0:<25s}'.format(k),end=' ')

    print('{0:>7.2f}'.format(v[0]),end=' ')

    print('{0:>10d}'.format(v[1]),end=' ')

    print('{0:>16.2f}'.format(v[2]))

    

print('Tax:{0:>57.2f}'.format(tax))

print('-'*65)

print('Amount Payable:{0:>46.2f}'.format(net))
