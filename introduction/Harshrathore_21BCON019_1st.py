ch=input("Enter a single charcter :")
if ch>='A' and ch<='Z':
    print("You entered an Upper Case character.")
elif ch>='a' and ch<='z':
    print("You entered a Lower Case character.")
elif ch>='0' and ch<='9':
    print("You entered a digit")
else:
    print("You entered a special character. ")
