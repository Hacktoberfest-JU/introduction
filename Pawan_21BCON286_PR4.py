def interestcalculator():
    c = 'y'
    while c == 'y':
        choice = input("Enter 1 to find Simple Interest\nEnter 2 to find Compound Interest \n : ").upper()
        print()
        if choice == '1':
            simpleinterest()

        elif choice == '2':
            compoundinterest()

        else:
            print("Invalid Input")
            exit()
    else:
        print('wrong input')


def simpleinterest():
    p = int(input("Enter Principle : "))
    r = int(input("Enter Rate of Interest : "))
    t = int(input("Enter Time Period : "))
    print("Simple Interest = ", p * r * t / 100)
    ad1 = input("Do you want to run the code again( ENTER Y IF YES ) : ").lower()
    if ad1 == "y":
        interestcalculator()
    else:
        exit()


def compoundinterest():
    p = int(input("Enter Principle : "))
    r = int(input("Enter Rate of Interest : "))
    t = int(input("Enter Time Period : "))
    print("Compound Interest = ", (p + p * r / 100) ** t)
    ad2 = input("Do you want to run the code again( ENTER Y IF YES ) : ").lower()
    if ad2 == "y":
        interestcalculator()
    else:
        exit()


interestcalculator()
