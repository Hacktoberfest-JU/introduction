def area():
    c = 'y'
    while c == 'y':
        choice = input("Select To find the area of\n1.CIRCLE\n2.RECTANGLE\n3.SQUARE\n4.TRIANGLE\n: ").upper()
        print()
        if choice == '1':
            circle()

        elif choice == '2':
            rectangle()

        elif choice == '3':
            square()

        elif choice == '4':
            triangle()
        else:
            print("Invalid Input")
            exit()
    else:
        print('wrong input')


def circle():
    # To find the area of circle
    r = float(input('Enter the radius of circle: '))
    print('The area of the given circle=', 22 / 7 * r ** 2)
    print()
    ad1 = input("Do you want to find area of other figure( ENTER Y IF YES ) : ").lower()
    if ad1 == "y":
        area()
    else:
        exit()


def rectangle():
    # To find the area of rectangle
    length = float(input('Enter the length of rectangle: '))
    breadth = float(input('Enter the breadth of rectangle: '))
    print('The area of rectangle=', length * breadth)
    print()
    ad2 = input("Do you want to find area of other figure( ENTER Y IF YES ) : ").lower()
    if ad2 == "y":
        area()
    else:
        exit()


def square():
    # To find the area of square
    s = float(input('Enter the side of square: '))
    print('The area of square=', s ** 2)
    print()
    ad3 = input("Do you want to find area of other figure( ENTER Y IF YES ) : ").lower()
    if ad3 == "y":
        area()
    else:
        exit()


def triangle():
    # To find the area of triangle
    b = float(input('Enter the base of triangle: '))
    h = float(input('Enter the height of triangle: '))
    print('The area of triangle=', 0.5 * b * h)
    print()
    ad4 = input("Do you want to find area of other figure( ENTER Y IF YES ) : ").lower()
    if ad4 == "y":
        area()
    else:
        exit()


area()

