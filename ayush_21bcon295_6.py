import random
import re
domino_set = []
y = -1
while y in range(-1, 7):
    y += 1
    for x in range(y, 7):
        domino_set.append([y, x])


def interface():
    print('=' * 70)
    print(f"Stock size: {len(stock_pieces)}\nComputer pieces: {len(computer_pieces)}")
    print()
    if len(domino_snake) > 6:
        print(
            f"{domino_snake[0]}{domino_snake[1]}{domino_snake[2]}...{domino_snake[-3]}{domino_snake[-2]}{domino_snake[-1]}")
    else:
        print(''.join([str(m) for m in domino_snake]))
    print()
    print('Your pieces:')
    for index, element in enumerate(player_pieces):
        print(f"{index + 1}:{element}")
    print()


def swap_left_move():  # Change orientation of domino
    if removed[-1] == domino_snake[0][0]:
        domino_snake.insert(0, removed)
    else:
        removed[0], removed[1] = removed[1], removed[0]
        domino_snake.insert(0, removed)


def swap_right_move():  # Change orientation of domino
    if removed[0] == domino_snake[-1][-1]:
        domino_snake.append(removed)
    else:
        removed[0], removed[1] = removed[1], removed[0]
        domino_snake.append(removed)


def move_player_func():
    global removed
    while True:
        move_player_str = input("Status: It's your turn to make a move. Enter your command.")
        # Input check 01
        if re.match("^[a-zA-Z]*$", move_player_str):
            print('Invalid input. Please try again.')
            continue
        move_player = int(move_player_str)
        # Input check 02
        if move_player not in range(-len(player_pieces), len(player_pieces) + 1):
            print('Invalid input. Please try again.')
            continue

        # Input condition 01
        if move_player in range(-len(player_pieces), 0):
            # Input check 03
            input_check_03 = None
            while True:
                if domino_snake[0][0] in player_pieces[abs(move_player) - 1]:
                    break
                else:
                    print('Illegal move. Please try again.')
                    input_check_03 = 'Failed'
                    break
            if input_check_03 != 'Failed':
                removed = player_pieces.pop(abs(move_player) - 1)
                swap_left_move()
                interface()
                break
            else:
                continue
        elif move_player in range(1, len(player_pieces) + 1):
            # Input check 03
            input_check_03 = None
            while True:
                if domino_snake[-1][-1] in player_pieces[move_player - 1]:
                    break
                else:
                    print('Illegal move. Please try again.')
                    input_check_03 = 'Failed'
                    break
            if input_check_03 != 'Failed':
                removed = player_pieces.pop(move_player - 1)
                swap_right_move()
                interface()
                break
            else:
                continue
        elif move_player == 0:
            from_stock = random.choice(stock_pieces)
            player_pieces.append(from_stock)
            stock_pieces.remove(from_stock)
            interface()
            break


def move_computer_func():
    global removed
    move_computer_line = input("Status: Computer is about to make a move. Press Enter to continue...")
    domino_snake_2 = []
    for r in domino_snake:
        for j in r:
            domino_snake_2.append(j)
    computer_pieces_2 = []
    for h in computer_pieces:
        for g in h:
            computer_pieces_2.append(g)
    num_score = {0: domino_snake_2.count(0) + computer_pieces_2.count(0),
                 1: domino_snake_2.count(1) + computer_pieces_2.count(1),
                 2: domino_snake_2.count(2) + computer_pieces_2.count(2),
                 3: domino_snake_2.count(3) + computer_pieces_2.count(3),
                 4: domino_snake_2.count(4) + computer_pieces_2.count(4),
                 5: domino_snake_2.count(5) + computer_pieces_2.count(5),
                 6: domino_snake_2.count(6) + computer_pieces_2.count(6)}
    pieces_score_list = []
    for q in range(0, len(computer_pieces_2), 2):
        pieces_score = num_score[computer_pieces_2[q]] + num_score[computer_pieces_2[q + 1]]
        pieces_score_list.append(pieces_score)
    draw_from_stock = None
    # Input condition 01
    while True:
        if max(pieces_score_list) == 0:
            draw_from_stock = 'yes'
            break
        checked_piece_score_index = pieces_score_list.index(max(pieces_score_list))
        pieces_score_list[checked_piece_score_index] = 0
        if domino_snake[0][0] in computer_pieces[checked_piece_score_index]:
            removed = computer_pieces.pop(checked_piece_score_index)
            swap_left_move()
            interface()
            break
        elif domino_snake[-1][-1] in computer_pieces[checked_piece_score_index]:
            removed = computer_pieces.pop(checked_piece_score_index)
            swap_right_move()
            interface()
            break
    if draw_from_stock == 'yes':
        from_stock = random.choice(stock_pieces)
        computer_pieces.append(from_stock)
        stock_pieces.remove(from_stock)
        interface()


def winning_conditions():
    global final_status
    draw_condition_8 = ''.join([str(m) for m in domino_snake]).count('1')
    player_pieces_1 = []
    for k in player_pieces:
        for m in k:
            player_pieces_1.append(m)
    if len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        final_status = 'player won'
        return True
    elif len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        final_status = 'computer_won'
        return True
    elif domino_snake[0][0] == domino_snake[-1][-1] and draw_condition_8 == 8:
        print("The game is over. It's a draw!")
        final_status = 'draw'
        return True
    elif len(stock_pieces) == 0 and (domino_snake[0][0] or domino_snake[-1][-1] not in [player_pieces_1]):
        print("The game is over. It's a draw!")
        final_status = 'draw'
        return True


while True:
    stock_pieces = random.sample(domino_set, 14)
    computer_pieces = random.sample([z for z in domino_set if z not in stock_pieces], 7)
    player_pieces = random.sample([z for z in domino_set if z not in stock_pieces + computer_pieces], 7)
    domino_snake = []
    start_piece = [6, 6] or [5, 5]
    final_status = None
    if start_piece in computer_pieces:
        computer_pieces.remove(start_piece)
        domino_snake.append(start_piece)
        interface()
        while True:
            if winning_conditions():
                break
            move_player_func()
            if winning_conditions():
                break
            move_computer_func()

    elif start_piece in player_pieces:
        player_pieces.remove(start_piece)
        domino_snake.append(start_piece)
        interface()
        while True:
            if winning_conditions():
                break
            move_computer_func()
            if winning_conditions():
                break
            move_player_func()

    if final_status is not None:
        break
