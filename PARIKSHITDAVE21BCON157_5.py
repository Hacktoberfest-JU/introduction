print("               JECRC UNIVERSITY")
l=[]
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Exit")
    a=int(input("Enter your choice:"))
    if a==1:
        x=int(input("Enter Book no. to insert:"))
        l.insert(0,x)
        print("Item Inserted Sucessfully")
        y=input("Want to print Queue?(Y/N)")
        if y == "y":
            print(l)
        else:
            continue
        
    elif a==2:
        l.pop(0)
        print("Item Dequeued sucessfully")
        y=input("Want to print Queue?(Y/N)")
        if y == "y":
            print(l)
        else:
            continue
    elif a==3:
        print("Thank you")
        break
    else:
        print("Wrong Input!!!!")
