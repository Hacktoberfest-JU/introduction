print("Press 1 for Square.")
print("Press 2 for Rectangle.")
print("Press 3 for Equilateral Triangle.")
print("Press 4 for Regular Pentagon.")
print("Press 5 for Regular Hexagon.")
print("Press 6 for Regular Heptagon.")
print("Press 7 for Regular Octagon.")
print("Press 8 for Regular Nonagon.")
print("Press 9 for Regular Decagon.")
print("Press 10 for Rohmbus.")
x=int(input("Enter your desired option:- "))
if x==1:
    print("You have selected Square.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length of side:- "))
        b=a*4
        print("The perimeter of square is",b)
    elif y==2:
        a=float(input("Enter length of side:- "))
        b=a*a
        print("The area of square is",b)
    else:
        print("Select a valid option.")
elif x==2:
    print("You have selected Rectangle.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length:- "))
        b=float(input("Enter breadth:- "))
        c=2*(a+b)
        print("The perimeter of rectangle is",c)
    elif y==2:
        a=float(input("Enter length:- "))
        b=float(input("Enter breadth:- "))
        c=a*b
        print("The area of rectangle is",c)
    else:
        print("Select a valid option.")
elif x==3:
    print("You have selected Equilateral Triangle.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length of side:- "))
        c=3*a
        print("The perimeter of equilateral triangle is",c)
    elif y==2:
        a=float(input("Enter length of side:- "))
        c=(1.732/4)*a**2
        print("The area of equilateral triangle is",c)
    else:
        print("Select a valid option.")
elif x==4:
    print("You have selected Regular Pentagon.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length of side:- "))
        c=5*a
        print("The perimeter of regular pentagon is",c)
    elif y==2:
        a=float(input("Enter apothem:- "))
        b=float(input("Enter length of side:- "))
        c=(5/2)*b*a
        print("The area of regular pentagon is",c)
    else:
        print("Select a valid option.")
elif x==5:
    print("You have selected Regular Hexagon.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length of side:- "))
        c=6*a
        print("The perimeter of regular hexagon is",c)
    elif y==2:
        b=float(input("Enter length of side:- "))
        c=(1.732*3/2)*b*b
        print("The area of regular hexagon is",c)
    else:
        print("Select a valid option.")
elif x==6:
    print("You have selected Regular Heptagon.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length of side:- "))
        c=7*a
        print("The perimeter of regular heptagon is",c)
    elif y==2:
        a=float(input("Enter apothem:- "))
        b=float(input("Enter length of side:- "))
        c=(7/2)*a*b
        print("The area of regular heptagon is",c)
    else:
        print("Select a valid option.")
elif x==7:
    print("You have selected Regular Octagon.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length of side:- "))
        c=8*a
        print("The perimeter of regular octagon is",c)
    elif y==2:
        b=float(input("Enter length of side:- "))
        c=(1+1.414)*2*b*b
        print("The area of regular octagon is",c)
    else:
        print("Select a valid option.")
elif x==8:
    print("You have selected Regular Nonagon.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length of side:- "))
        c=9*a
        print("The perimeter of regular nonagon is",c)
    elif y==2:
        a=float(input("Enter apothem:- "))
        b=float(input("Enter length of side:- "))
        c=(9*b*a)/2
        print("The area of regular nonagon is",c)
    else:
        print("Select a valid option.")
elif x==9:
    print("You have selected Regular Decagon.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length of side:- "))
        c=10*a
        print("The perimeter of regular decagon is",c)
    elif y==2:
        b=float(input("Enter length of side:- "))
        c=(5/2)*b*b*3.077
        print("The area of regular decagon is",c)
    else:
        print("Select a valid option.")
elif x==10:
    print("You have selected Rhombus.")
    print("Press 1 for Perimeter.")
    print("Press 2 for Area.")
    y=int(input("Enter your desired option:- "))
    if y==1:
        a=float(input("Enter length of side:- "))
        c=4*a
        print("The perimeter of regular hexagon is",c)
    elif y==2:
        a=float(input("Enter length of diagonal 1:- "))
        b=float(input("Enter length of diagonal 2:- "))
        c=a*b
        print("The area of rhombus is",c)
    else:
        print("Select a valid option.")
    print("Thank you for using our program.")
else:
    print("Enter a valid option.")
