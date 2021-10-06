
#sp:selling price cgst:central govt gst  sgst:state gov gst
a=input("enter item name: ")
b=float(input("enter selling price of the item "+a+":"))
r=float(input("enter gst rate(in %)"))
y=b*((r/2)/100)
p=y
t=b+p+y


print("\t INVOICE")
print("Price:",b)
print("CGST:",p)
print("SGST:",y)
print("Amount Payable:",t)
