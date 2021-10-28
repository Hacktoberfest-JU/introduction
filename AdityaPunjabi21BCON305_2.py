print("Press 1 for Perimeter of Square.")
print("Press 2 for Area of Square.")
z=int(input("Enter a valid option :- "))
x=float(input("Enter size of edge :- "))
if z==1:
    y=4*x
    print("Perimeter of given square is",y,".")
elif z==2:
    y=x**2
    print("Area of given square is",y,".")
else:
    print("Please enter a valid option☻☻")
