import random
print("****  WELCOME TO THE GAME  ****")
print("Press 1 for Rock")
print("Press 2 for Paper")
print("Press 3 for Scissor")
x=int(input("Choose any one :- "))

y = random.randrange(1,4)
# 1 = Rock , 2 = Paper , 3 = Scissor

if x==1 or x==2 or x==3:
    if x == y:
        print("Its a Tie")
    
    elif x==1:
        if y ==2 :
            print("You Lose")
            print("You Chose Rock and the Bot Chose Paper")
        elif y == 3:
            print("Congratulations! You Won")
            print("You Chose Rock and the Bot Chose Scissor")

    elif x == 2:
        if y == 1:
            print("Congratulations! You Won")
            print("You Chose Paper and the Bot Chose Rock")
        elif y == 3:
            print("You Lose")
            print("You Chose Paper and the Bot Chose Scissor")

    elif x == 3:
        if y == 1:
            print("You Lose")
            print("You Chose Scissor and the Bot Chose Rock")
        elif y == 2:
            print("Congratulations! You Won")
            print("You Chose Scissor and the Bot Chose Paper")      
else:
    print("Please Choose Again")
