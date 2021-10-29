#MY NAME IS AYUSH SINGHAL 
#THIS CODE CONSISTS OF VAROIUS USE OF RANDOM MODULE

#THE PERFECT GUESS
def perguess():
    import random 
    randnum = random.randint(1,11)
    user_guess = 0
    guess = 0
    while user_guess != randnum:
        guess = guess + 1 
        user_guess = int(input("Enter the number : "))
        if user_guess != randnum :
            if randnum > user_guess  :
                print ("You guessed it wrong :(, Try to guess higher :P") 
            else :
                print ("You guesssed it wrong :(, Try to guess lower :b")
        else :
            print ("You guessed it right :), You took, ", guess, "guesses")

#WHO GOT THE BAT
def rock():
    print('''   1 is for rock!!
        2 is for Paper!!
        3 is for Scissor!!
        4 is for Exit''')
    import random
    randnum = random.randint(1,4)
    user = int(input("Enter the number : "))
    if randnum == 1 and user == 2 :
        print("The user won :)")
        print("Computer guessed ", randnum)
    elif randnum == 1 and user == 3 :
            print("The computer won :(")
            print("Computer guessed ", randnum)
    elif randnum == 2 and user == 1 :
            print("The computer won :(")
            print("Computer guessed ", randnum)
    elif randnum == 2 and user == 3 :
            print("The user won :)")
            print("Computer guessed ", randnum)
    elif randnum == 3 and user == 1 :
            print("The computer won :)")
            print("Computer guessed ", randnum)
    elif randnum == 3 and user == 2 : 
            print("The computer won :)")
            print("Computer guessed ", randnum)
    elif randnum == user : 
            print("Its a draw gyus :!")
    else :
            print("Please enter a number from 1, 2, 3, 4 only :!")
 
#THE ULTIMATE FIGHT
#HUMAN VS MACHINE

def match():
        import random 
        randnum = random.randint(1,11)
        print(randnum)
        ranum = random.randint(1,11)
        user = int(input("Enter a number between 1-11 : "))
        if ranum == randnum and user == randnum :
                        print("This will never end :")
        elif ranum  == randnum :
                        print("Machine won :( KO")
        elif user == randnum :
                        print("Human won :) ko")
        elif user >= 12 or user <= 0 :
                        print("Human!!, Be in your limits :!")
        else :
                        print("AAH, shit, here we go again")
            

print("These are some simple uses of random module")
print("Choose your choice between 1 - 3")
print("1. The perfect guess")
print("2. Who got the bat")
print("3. The ultimate fight")
print("4. Exit")
choice = int(input("Please enter your choice from the above given option: "))
if choice == 1 :
        perguess()
elif choice == 2 :
        rock()
elif choice == 3:
        match()
else :
        print("Please enter a valid number :|")
        


     
     
              

        
