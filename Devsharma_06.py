#This is a Seven Up-Seven Down Game Made By DEV SHARMA
import random
print("-------------------------------------------------------------")
print("    Welcome to Seven Up-Seven Down Game Made By DEV SHARMA")
print("-------------------------------------------------------------")
print("🌟 If your Pridiction of Seven upordown Got Correct then you'll get Double the Amount you Applied(2x) \n"
      "🌟 if your Pridiction of Seven Get Correct you'll get Tripple the amount you applied(3x)\n"
      "🌟 If your Pridication GOt Inccorect your Money will be Gone and Not Be Refundable")
totalmoney = 0
n = 0
while n==0:
    print("-----------------------------------------------------------")
    while (True):
        print("Enter the Money you want to Apply(rs10-rs10k),Currently You are having Rs.", totalmoney,
              "in your Game Account :- ",end=' ')
        money = int(input())
        if money not in range(0,10000):
            print("Enter a Non-Zero and Positive Number")
        else:
            break
    print()
    n = int(input("Predict....\n1. SEVEN UPS\n2. SEVEN DOWN\n3. SEVEN\nYour Choise :-"))
    print("-----------------------------------------------------------")

    l = [1,2,3,4,5,6,7,8,9,10,11,12]
    Dice_Number = (random.choice(l))
    print("DICE ROLLED SCORE :- ", Dice_Number)
    if n == 1 and Dice_Number>7:
        print("Congratulation you Won This Game, You have Applied Rs.",money,"and Now You Will be Geting rs.",money*2,"(Double the Amount you Applied)")
        totalmoney = money*2
    elif n==2 and  Dice_Number<7:
        print("Congratulation you Won This Game, You have Applied Rs.", money, "and Now You Will be Geting rs.", money * 2,
              "(Double the Amount you Applied)")
        totalmoney = money * 2
    elif n==3 and Dice_Number ==7:
        print("Congratulation you Won This Game, You have Applied Rs.", money, "and Now You Will be Geting rs.", money * 3,
              "(Tripple the Amount you Applied)")
        totalmoney = money * 3
    else:
        print("You Lost this Game")
        totalmoney = totalmoney-money
    print("-----------------------------------------------------------")
    print("Now, you have Rs.",totalmoney,"in your Game Account")
    choise = int(input("1. Do you want to Withdrawal your money\n2. Do you want to Play More\nYour Choise :- "))
    if choise ==1:
        if totalmoney >0:
            print("-----------------------------------------------------------")
            print("Congratulation, Your Rs.",totalmoney,"has been Transferred to your Bank Account")
            print("-----------------------------------------------------------")
            n+=1
        else:
            print("-----------------------------------------------------------")
            print("Opps, Your cureent Game Acount Balance is Rs.", totalmoney,"So it can't be Transfered to Bank Account")
            print("-----------------------------------------------------------")
            n+=1
        print("Thanks For Using Seven Up-Seven Down Game Made By DEV SHARMA")
    if choise ==2:
       n =0
