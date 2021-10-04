import random
Number=random.randrange(0,101)
Guess=int(input("Guess a Number Between 0 and 100 --> "))
while Guess!=Number:
    if Guess<=Number:
        print("Plz Enter A Greater Number!! ☻☻")
        Guess=int(input("Guess a Number Between 0 and 100 --> "))
    else:
        print("You Need to Guess A Lower Number, Try Again☻☻")
        Guess=int(input("Guess a Number Between 0 and 100 --> "))
print("Congratulations You Guessed the Number Correctly And You Won The Game☻☻☻☻")
