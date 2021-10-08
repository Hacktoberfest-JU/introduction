import datetime  
now=datetime.datetime.now()
dtm=str(now)
print("\tWelcome to Ours Variety Store")
item=input('Enter Item Name :- ')
qty=int(input('Enter How Many/Much You Want:- '))
price=int(input('Enter the Price:-'))
val=price*qty
tax=val*0.05
net=val+tax
print("-"*60)
print("\t\t\t\tINVOICE")
print()
print("date : {0:>55s}".format(dtm))
print("-"*60)
print("ITEM\t\t\t  Unit Price\tQuantity     Value")
print("-"*60)
print("{0:<25s}".format(item),end=" ")
print("{0:>7.2f}".format(price),end=" ")
print("{0:>10d}".format(qty),end=" ")
print("{0:>14.2f}".format(val))
