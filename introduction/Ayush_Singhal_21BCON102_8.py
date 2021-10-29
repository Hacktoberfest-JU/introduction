#MY NAME IS AYUSH SINGHAL
#THIS CODE SHOWS HPW TP EXTERNALLY SURPASS ERROR, AND SHOW MORE EASY SOFTWARE TO USER
while(True):
    print("Type q if you want to exit the program ")
    a = input("Enter your age : ")
    if  a == 'q' or a == 'Q' :
        break
    try:
        a = int(a)
        if a >= 18 :
            print("You are eligible to vote :) ")
        else :
            print("You are not eligible to vote :( ")
    except Exception as e :
        print("Your input is wrong ")
print("Thanks for the support :))")
    

