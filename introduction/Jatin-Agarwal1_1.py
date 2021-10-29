# Stone Paper Scissor
import random as rd

score = [0,0] # bot,player
choices = ["stone","paper","scissor"]

while 1:
    print("choose stone, paper or scissor\n")
    choice = input().casefold()
    while choice not in choices:
        print("please enter valid input")
        choice = input().casefold()
    bot = rd.choice(choices)
    print(f"Bot chooses {bot}")
    if choice == bot:
        pass
    elif choice == choices[0]:
        if bot == choices[1]:
            score[0] += 1
        else:
            score[1] += 1
    elif choice == choices[1]:
        if bot == choices[2]:
            score[0] += 1
        else:
            score[1] += 1
    elif choice == choices[2]:
        if bot == choices[0]:
            score[0] += 1
        else:
            score[1] += 1
    print(f"Score:\nBot {score[0]}\nPlayer {score[1]}") 
        

