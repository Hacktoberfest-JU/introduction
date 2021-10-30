totaltrans, totalsales=0,0
count=1
while count<=7:
    trans=int(input("Transactions made on day" +str(count) +" :- "))
    items= int(input("Items sold a day"+ str(count)+" :- "))
    totaltrans+=trans
    totalsales+=items
    count+=1
avgsales=totaltrans/totalsales #sales per transaction
print("Total Sales made:- ",totalsales)
print("Total Transaction made:- ", totaltrans)
print("Average Sales per transaction:- ",avgsales)
