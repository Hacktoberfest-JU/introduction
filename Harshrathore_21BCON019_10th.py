#To check if the program is 1,2,3 digit

#Taking input from user
num = int(input("Enter number : "))

#for input less than 0
if num<0:
    print("Invalid Entry. Valid range is 0 to 999.")

#For single digit number
elif num<10:
    print("Single digit number is entered.")

#For two digit number
elif num<100:
    print("Two digit number is entered.")

#For three digit number
elif num<1000:
    print("Three digit number is entred.")

#For all other cases
else:
    print("Invalid Entry. Valid range is 0 to 999.")
