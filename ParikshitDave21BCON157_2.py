#This programme tells us that the given year is leap or not 
year = int(input("enter year:"))
if year % 4 == 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
