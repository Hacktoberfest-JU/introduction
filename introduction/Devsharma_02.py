a = int(input("enter the 1st no. :- "))
b = int(input("enter the 2nd no. :- "))
c = input("enter the opreator :- ")
if c == "+":
    r = a+b
elif c == "-":
    r = a -b
elif c == "*":
    r = a *b
elif c == "/":
    r = a /b
elif c == "**":
    r = a**b
else :
    print("enter the correct arthematic operator")
print("ANSWER --> ",r)
