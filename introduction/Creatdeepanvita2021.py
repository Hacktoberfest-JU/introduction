import pandas as pd
import csv,os,datetime
import time
import matplotlib.pyplot as plt
filename="C:\\Users\\Admin\\Desktop\\itemsTest.csv"
salesCSV="C:\\Users\\Admin\\Desktop\\Sales.csv"

print("\n----------Charley's Home Bakery----------")
print("\nEnter 1 for Customer Order.")
print("Enter 2 for Store Management System.")
ch=input("Enter your choice : ")

#customer order
if ch=='1':
    print("\n----------Welcome to Charley's Home Bakery----------")
    print("\nBelow are the avialable products, please enter your order.\n")
    orderDF=pd.DataFrame(columns=['Name','Price','Quantity','Amount'])
    inventoryDF=pd.read_csv(filename)
    i=0
    total=0
    #Loop to process order
    print('\n**ENTER CUSTOMER ORDER DETAILS**')
    while True:
        print("------------------------------------------")    
        print("\t* * LIST OF ITEMS * *")
        print("------------------------------------------")    
        print("\n",inventoryDF.to_string(index=False))
        print("------------------------------------------")    
        ordDetail=[]
        iCode=int(input("Enter the item code: "))
        if (iCode in inventoryDF['Item Code'].values):                
            temp=inventoryDF[inventoryDF['Item Code']==iCode]
            ind=temp.index[0]
            iName=temp.Name[ind]
            iPrice=temp.Price[ind]
            iStock=temp.Stock[ind]
            if iStock==0:
                print("=========Item out of stock=========") 
                print("~ ~ ~ ~ SELECT ANOTHER ITEM ~ ~ ~ ~\n") 
                continue
            while True:
                qty=int(input("Enter purchase quantity: "))
                if qty>iStock:
                    print("Please enter quantity less than or equal to stock available.")
                    continue
                else:
                    break
            ordDetail.append(iName)
            ordDetail.append(iPrice)
            ordDetail.append(qty)
            amt=iPrice*qty
            ordDetail.append(amt)
            #Add a new row 
            orderDF.loc[i]=ordDetail
            total=total+amt
            SGST=total*9/100
            CGST=total*9/100
            pay_Amt=0
            pay_Amt=total+SGST+CGST
            i+=1
#updating inventory                
            inventoryDF.iat[ind,3]-=qty
            inventoryDF.to_csv(filename,index=False)  
        else:
            print("Invalid Item Code")
        choice=input("PRESS N TO FINISH ORDER - ")
        if choice=='N' or choice=='n':
            break
#loop ends
#updating sales CSV file
    if os.path.isfile(salesCSV)==True:
        orderDF.to_csv(salesCSV,index=False,mode='a',header=False)
    else:
        orderDF.to_csv(salesCSV,index=False,mode='a',
        header=['Name','Price','Quantity','Amount'])
    print('-------------------------------------------------------------')
    print(datetime.date.today(),'\t\tBILL')        
    print('-------------------------------------------------------------')
    print("\n",orderDF)
    print("\nSGST  @9% :",SGST)
    print("CGST  @ 9% :",CGST)
    print('-------------------------------------------------------------')
    print("You have to pay Rs.",round(pay_Amt))
    print("\nThank you for visiting Charley's Home Bakery. Visit Again.")
    print('-------------------------------------------------------------')
    
#store management system    
if ch=='2':
    while True:
        print("\n*********************************************")
        print("\n*   WELCOME TO CHARLIE'S HOME BAKERY    *")
        print("\n*********************************************")
        print("PRESS 1 TO ADD NEW ITEMS")
        print("PRESS 2 TO CHANGE ITEM DETAILS")
        print("PRESS 3 TO REMOVE ITEMS")
        print("PRESS 4 TO DISPLAY INVENTORY")
        print("PRESS 5 FOR INVENTORY ANALYSIS")
        print("PRESS 6 FOR DATA VISUALISATION")
        print("PRESS ANY KEY TO EXIT THE STORE MANAGEMENT SYSTEM")
        print("*********************************************")
        ch=input("Enter your choice : ")
        if ch=='1':
            #ADD ITEMS
            print("\n**ADD NEW ITEMS**")
            if os.path.isfile(filename)==True:
                itemslist=[]
                #Automatically generating the Item Code
                maxIcodeDF=pd.read_csv(filename,usecols=[0])
                print(maxIcodeDF)
                itemCode=maxIcodeDF['Item Code'].max()+1
            else:
                #Add header row
                itemslist=[['Item Code','Name','Price','Stock','Category']]
                itemCode=1
            while True:
                item=[]
                item.append(itemCode)
                item.append(input("Enter item name : "))
                item.append(input("Enter item price : "))
                item.append(input("Enter item stock : "))
                item.append(input("Enter item category : "))
                print(item)
                itemslist.append(item)
                choice=input("PRESS N TO STOP ENTERING MORE ITEMS - ")
                if choice=='N' or choice=='n':
                    break
                itemCode+=1
            # Appends items in the csv file
            with open(filename, "a",newline="") as f:
                itemWriter = csv.writer(f)
                itemWriter.writerows(itemslist)
    
        elif ch=='2':
            if os.path.isfile(filename)==False:
                print("Items file does not exist")
                time.sleep(4)
                continue
            inventoryDF=pd.read_csv(filename)
            if inventoryDF.empty:
                print(inventoryDF)
                print("\nNo items to modify.")
                time.sleep(4)
                continue 
            print("\n**ITEMS IN THE STORE**")
            print(inventoryDF)
            itemCode=int(input("\nEnter the code of the item to be modifed : "))
            
            if itemCode in inventoryDF['Item Code'].values:
                while True:
                    temp=inventoryDF[inventoryDF['Item Code']==itemCode]
                    print('--------------------------------------------------')
                    print(temp)
                    print('--------------------------------------------------')
                    #temp.index retrieves the row indexes as a list
                    #temp.index[0] retrieves the first item from the list
                    ind=temp.index[0]  
                    itmName=input("Enter item name : ")
                    itmPrice=int(input("Enter item price : "))
                    itmStock=int(input("Enter item stock : "))
                    itmCatg=input("Enter item category : ")
                    inventoryDF.iat[ind,1]=itmName            
                    inventoryDF.iat[ind,2]=itmPrice
                    inventoryDF.iat[ind,3]=itmStock
                    inventoryDF.iat[ind,4]=itmCatg
                    inventoryDF.columns=['Item Code','Name','Price',"Stock",'Category']
                    inventoryDF.to_csv(filename,index=False)
                    ContMod=input("\nPress 'Y' to continue modifying items : ")
                    if ContMod=='y' or ContMod=='Y':
                        print(inventoryDF)
                        itemCode=int(input("\nEnter the code of the item to be modifed : "))
                        continue
                    else:
                        break
            else:
                print("Invalid Item Code")
    
        elif ch=='3':
            if os.path.isfile(filename)==False:
                print("Items file does not exist")
                time.sleep(4)
                continue 
            inventoryDF=pd.read_csv(filename)
            if inventoryDF.empty:
                print(inventoryDF)
                print("\nNo items to delete.")
                time.sleep(4)
                continue                        
            print("\n**ITEMS IN THE STORE**")
            print(inventoryDF)
            itemCode=int(input("\nEnter the item code to deleted : "))
            if itemCode in inventoryDF['Item Code'].values:
                while True:
                    temp=inventoryDF[inventoryDF['Item Code']==itemCode]
                    print(temp)
                    ind=temp.index[0]
                    print(ind)
                    inventoryDF.drop(ind,inplace=True)
                    print(inventoryDF)
                    inventoryDF.to_csv(filename,index=False)
                    ContDel=input("\nPress 'Y' to delete more items.\t")
                    if ContDel=='y' or ContDel=='Y':
                        itemCode=int(input("\nEnter the code of the item to be deleted : "))
                        continue
                    else: 
                        break
            else:
                print("Invalid Item Code")            
                
        elif ch=='4':
            if os.path.isfile(filename)==False:
                print("Items file does not exist")
                time.sleep(4)
                continue
            inventoryDF=pd.read_csv(filename)
            if inventoryDF.empty:
                print("\nNo items present in the store.")
                time.sleep(4)
                continue
            print('--------------------------------------------------')
            print("\t**LIST OF ITEMS IN THE STORE**")
            print('--------------------------------------------------')
            print(inventoryDF)
            print('--------------------------------------------------')
            
        elif ch=='5':
            if os.path.isfile(filename)==False:
                input("Items file does not exist.\nPress any key to continue...")
                continue
            inventoryDF=pd.read_csv(filename)
            if inventoryDF.empty:
                print("Data unavailable.")
            else:
                print("\n**DATA ANALYSIS**")
                print("\n1. Display TOP n ITEMS.")
                print("\n2. Display BOTTOM n ITEMS.")
                print("\n3. SORT ITEMS on the basis of price.")
                print("\n4. SORT ITEMS on the basis of stock available.")
                ch=int(input("\nEnter your choice : "))
                if ch==1:
                    n=int(input("Enter the number of items to be displayed : "))
                    print(inventoryDF.head(n))
                elif ch==2:
                    n=int(input("Enter the number of items to be displayed : "))
                    print(inventoryDF.tail(n))
                elif ch==3:
                    df=inventoryDF.sort_values('Price',ascending=False)
                    print(df.to_string(index=False))
                elif ch==4:
                    df=inventoryDF.sort_values('Stock',ascending=False)
                    print(df.to_string(index=False))
                
        elif ch=='6':
            inventoryDF=pd.read_csv(filename)
            if os.path.isfile(filename)==False:
                input("Items file does not exist.\nPress any key to continue...")
                continue
            if inventoryDF.empty:
                print("Data unavailable.")
            else:
                while True:
                    print("\n**DATA VISUALISATION**")
                    print("\nEnter 'P' to visualise data on basis of Price.")
                    print("Enter 'S' to visualise data on basis of Stock.")
                    ch=input("\nEnter your choice : ")
                    if ch=='P' or ch=='p':
                      print("\n ITEM PRICE BAR CHART")
                      inventoryDF.plot(kind='bar',x='Name',y='Price',title='Item Price Analysis')
                      plt.xlabel('Names of items')
                      plt.ylabel('Price')
                      plt.show()
                    if ch=='S' or ch=='s':
                      print("\n ITEM STOCK BAR CHART")
                      inventoryDF.plot(kind='bar',x='Name',y='Stock',title='Item Stock Analysis')
                      plt.xlabel('Names of items')
                      plt.ylabel('Stock available')
                      plt.show() 
                    else:
                        print("Invalid choice.")
                        break
        else: 
            break
        input('Press any key to continue...')
        #end of main loop
    print('You have exited the store management system.')            
