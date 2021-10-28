# Starting Blank Grid
user_input = '         '
z11 = user_input[0]
z12 = user_input[1]
z13 = user_input[2]
z21 = user_input[3]
z22 = user_input[4]
z23 = user_input[5]
z31 = user_input[6]
z32 = user_input[7]
z33 = user_input[8]
print('---------')
line_1 = [['|', z11, z12, z13, '|'], ['|', z21, z22, z23, '|'], ['|', z31, z32, z33, '|']]
for x in line_1:
    print(' '.join(x))
print('---------')


def input_condition():
    global move_input
    move_input = input('Enter the coordinates: ')
    i = 0
# Input Condition 01
    while i < 2:
        i += 1
        while move_input == 'one' or move_input == 'one one' or move_input == 'one two' or move_input == 'one three':
            print('You should enter numbers!')
            move_input = input('Enter the coordinates: ')
        while move_input == 'two' or move_input == 'two one' or move_input == 'two two' or move_input == 'two three':
            print('You should enter numbers!')
            move_input = input('Enter the coordinates: ')
        while move_input == 'three' or move_input == 'three one' or move_input == 'three two' or move_input == 'three three':
            print('You should enter numbers!')
            move_input = input('Enter the coordinates: ')
# Input Condition 02
        move_input_row = int(move_input[0])
        move_input_column = int(move_input[2])
        while move_input_row > 3 or move_input_column > 3:
            print('Coordinates should be from 1 to 3!')
            move_input = input('Enter the coordinates: ')
            move_input_row = int(move_input[0])
            move_input_column = int(move_input[2])
            if move_input_row <= 3 and move_input_column <= 3:
                break
# Input Condition 03
        while True:
            if move_input == '1 1' and z11 != ' ':
                print('This cell is occupied! Choose another one!')
                move_input = input('Enter the coordinates: ')
            elif move_input == '1 2' and z12 != ' ':
                print('This cell is occupied! Choose another one!')
                move_input = input('Enter the coordinates: ')
            elif move_input == '1 3' and z13 != ' ':
                print('This cell is occupied! Choose another one!')
                move_input = input('Enter the coordinates: ')
            elif move_input == '2 1' and z21 != ' ':
                print('This cell is occupied! Choose another one!')
                move_input = input('Enter the coordinates: ')
            elif move_input == '2 2' and z22 != ' ':
                print('This cell is occupied! Choose another one!')
                move_input = input('Enter the coordinates: ')
            elif move_input == '2 3' and z23 != ' ':
                print('This cell is occupied! Choose another one!')
                move_input = input('Enter the coordinates: ')
            elif move_input == '3 1' and z31 != ' ':
                print('This cell is occupied! Choose another one!')
                move_input = input('Enter the coordinates: ')
            elif move_input == '3 2' and z32 != ' ':
                print('This cell is occupied! Choose another one!')
                move_input = input('Enter the coordinates: ')
            elif move_input == '3 3' and z33 != ' ':
                print('This cell is occupied! Choose another one!')
                move_input = input('Enter the coordinates: ')
            else:
                break


while True:
# Input Condition for 'X'
    input_condition()
# Input for 'X'
    if move_input == '1 1':
        print('---------')
        line_1 = [['|', 'X', z12, z13, '|'], ['|', z21, z22, z23, '|'], ['|', z31, z32, z33, '|']]
        z11 = 'X'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '1 2':
        print('---------')
        line_1 = [['|', z11, 'X', z13, '|'], ['|', z21, z22, z23, '|'], ['|', z31, z32, z33, '|']]
        z12 = 'X'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '1 3':
        print('---------')
        line_1 = [['|', z11, z12, 'X', '|'], ['|', z21, z22, z23, '|'], ['|', z31, z32, z33, '|']]
        z13 = 'X'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '2 1':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', 'X', z22, z23, '|'], ['|', z31, z32, z33, '|']]
        z21 = 'X'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '2 2':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, 'X', z23, '|'], ['|', z31, z32, z33, '|']]
        z22 = 'X'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '2 3':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, z22, 'X', '|'], ['|', z31, z32, z33, '|']]
        z23 = 'X'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '3 1':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, z22, z23, '|'], ['|', 'X', z32, z33, '|']]
        z31 = 'X'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '3 2':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, z22, z23, '|'], ['|', z31, 'X', z33, '|']]
        z32 = 'X'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '3 3':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, z22, z23, '|'], ['|', z31, z32, 'X', '|']]
        z33 = 'X'
        for x in line_1:
            print(' '.join(x))
        print('---------')
# Winning Conditions for 'X'
    if z11 == z12 == z13 == 'X' or z21 == z22 == z23 == 'X' or z31 == z32 == z33 == 'X' or z11 == z21 == z31 == 'X' or z12 == z22 == z32 == 'X' or z13 == z23 == z33 == 'X' or z11 == z22 == z33 == 'X' or z13 == z22 == z31 == 'X':
        print('X wins')
        break
# For Draw
    elif z11 != ' ' and z12 != ' ' and z13 != ' ' and z21 != ' ' and z22 != ' ' and z23 != ' ' and z31 != ' ' and z32 != ' ' and z33 != ' ':
        print('Draw')
        break

# Input Condition for 'O'
    input_condition()
# Input for 'O'
    if move_input == '1 1':
        print('---------')
        line_1 = [['|', 'O', z12, z13, '|'], ['|', z21, z22, z23, '|'], ['|', z31, z32, z33, '|']]
        z11 = 'O'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '1 2':
        print('---------')
        line_1 = [['|', z11, 'O', z13, '|'], ['|', z21, z22, z23, '|'], ['|', z31, z32, z33, '|']]
        z12 = 'O'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '1 3':
        print('---------')
        line_1 = [['|', z11, z12, 'O', '|'], ['|', z21, z22, z23, '|'], ['|', z31, z32, z33, '|']]
        z13 = 'O'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '2 1':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', 'O', z22, z23, '|'], ['|', z31, z32, z33, '|']]
        z21 = 'O'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '2 2':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, 'O', z23, '|'], ['|', z31, z32, z33, '|']]
        z22 = 'O'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '2 3':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, z22, 'O', '|'], ['|', z31, z32, z33, '|']]
        z23 = 'O'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '3 1':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, z22, z23, '|'], ['|', 'O', z32, z33, '|']]
        z31 = 'O'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '3 2':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, z22, z23, '|'], ['|', z31, 'O', z33, '|']]
        z32 = 'O'
        for x in line_1:
            print(' '.join(x))
        print('---------')
    elif move_input == '3 3':
        print('---------')
        line_1 = [['|', z11, z12, z13, '|'], ['|', z21, z22, z23, '|'], ['|', z31, z32, 'O', '|']]
        z33 = 'O'
        for x in line_1:
            print(' '.join(x))
        print('---------')
# Winning Condition for 'O'
    if z11 == z12 == z13 == 'X' or z21 == z22 == z23 == 'O' or z31 == z32 == z33 == 'O' or z11 == z21 == z31 == 'O' or z12 == z22 == z32 == 'O' or z13 == z23 == z33 == 'O' or z11 == z22 == z33 == 'O' or z13 == z22 == z31 == 'O':
        print('O wins')
        break
# Continue statement to repeat loop
    elif ' ' in user_input:  # Game not finished
        continue
