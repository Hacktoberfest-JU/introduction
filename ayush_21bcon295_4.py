import random
import re


def game():
    print()
    word_list = ('python', 'java', 'kotlin', 'javascript')
    word = random.choice(word_list)
    hidden_word = '-' * len(word)
    print(hidden_word)
    hidden_word_list = []
    for k in hidden_word:
        hidden_word_list.append(k)
    guessed_words = set()
    tries = 8
    while tries > 0:
        user_input = input('Input a letter: ')
        set_1 = set(word)
        # Input Check
        if len(user_input) != 1:
            print('You should input a single letter')
            print()
            print(''.join(hidden_word_list))
            continue
        elif not re.match('[a-z]', user_input):
            print('Please enter a lowercase English letter')
            print()
            print(''.join(hidden_word_list))
            continue
        # Input Function
        if user_input in hidden_word_list:
            print("You've already guessed this letter")
        elif user_input in guessed_words:
            print("You've already guessed this letter")
        elif user_input in set_1:
            for x, y in enumerate(word):
                if y == user_input:
                    hidden_word_list[x] = y
            # Winning Condition
            if ''.join(hidden_word_list) == word:
                print()
                print(''.join(hidden_word_list))
                print('You guessed the word!')
                print('You survived!')
                print()
                break
        else:
            print("That letter doesn't appear in the word")
            tries -= 1
            guessed_words.add(user_input)
        if tries != 0:
            print()
            print(''.join(hidden_word_list))
    # Losing Condition
    if '-' in hidden_word_list:
        print('You lost!')
        print()


print('H A N G M A N')
while True:
    game_status = input('Type "play" to play the game, "exit" to quit: ')
    if game_status == 'play':
        game()
    elif game_status == 'exit':
        break
