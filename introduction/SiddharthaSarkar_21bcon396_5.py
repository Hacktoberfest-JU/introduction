def add(x,y):
    return x+y

def sub (x,y):
    return x-y

def multi (x,y):
    return x*y

def div (x,y):
    return x/y

print("Please select operations:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice = input("Enter your choice(1,2,3,4):")

    if choice in ('1','2','3','4'):
        num1=float(input("Enter number 1:"))
        num2=float(input("Enter number 2:"))

        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))

        elif choice=='2':
            print(num1,"-",num2,"=",sub(num1,num2))

        elif choice=='3':
            print(num1,"*",num2,"=",multi(num1,num2))

        elif choice=='4':
            print(num1,"/",num2,"=",div(num1,num2))

        break
    else:
        print("INVALID INPUT")
