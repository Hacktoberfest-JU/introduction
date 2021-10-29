print("!!Temperature Conversion Calculator!!")
print("Press 1 for Celsius to Kelvin.")
print("Press 2 for Kelvin to Celsius.")
print("Press 3 for Celsius to Fahrenheit.")
print("Press 4 for Fahrenheit to Celsius.")
print("Press 5 for Kelvin to Fahrenheit.")
print("Press 6 for Fahrenheit to Kelvin.")
x=int(input("Enter option :- "))
if x==1:
    y=float(input("Enter temperature in Celsius :- "))
    z=y+273
    print("The temperature in kelvin is",z)
elif x==2:
    y=float(input("Enter temperature in Kelvin :- "))
    z=y-273
    print("The temperature in celsius is",z)
elif x==3:
    y=float(input("Enter temperature in Celsius :- "))
    z=(y*9/5)+32
    print("The temperature in fahrenheit is",z)
elif x==4:
    y=float(input("Enter temperature in Fahrenheit :- "))
    z=(y-32)*(5/9)
    print("The temperature in celsius is",z)
elif x==5:
    y=float(input("Enter temperature in Kelvin :- "))
    z=(y-273)*(9/5)+32
    print("The temperature in fahrenheit is",z)
elif x==6:
    y=float(input("Enter temperature in Fahrenheit :- "))
    z=(y-32)*(5/9)+273
    print("The temperature in kelvin is",z)
else:
    print("Please enter a valid option.")
print("☻☻☻☻Thank you for using our program☻☻☻☻")
