#to calculate the sum of no entered until user stop entering more no
count=sum=0
ans='y'
while ans=='y':
    num=int(input("Enter number:"))
    sum=sum+num
    count=count+1
    print("The sum of the no entered is ",sum)
    ans=input("Want to enter more no?(y/n):")
 
else:    
     print("You entered",count,"nos so far")

print("Sum of numbers entered is ",sum)
     
        
        
