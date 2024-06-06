# initializing which shape is for which player
p1_shape = 'X'
p2_shape = 'O'

# the spaces where you can place the shape (key=space, value=shape) 
spaces = {'TL':' ',
          'TC':' ',
          'TR':' ',
          'ML':' ',
          'MC':' ',
          'MR':' ',
          'BL':' ',
          'BC':' ',
          'BR':' ' } 


def show_grid():

    print()
    print('Grid:')
    print()
    print(f"{spaces['TL']}|{spaces['TC']}|{spaces['TR']}")
    print("_ _ _")
    print(f"{spaces['ML']}|{spaces['MC']}|{spaces['MR']}")
    print("_ _ _")
    print(f"{spaces['BL']}|{spaces['BC']}|{spaces['BR']}")
    print()


def end_of_game():

    # if there are 3 'X's on a line, finishes the game, displays winner
    if spaces['TL']==spaces['TC']==spaces['TR']=='X' or spaces['ML']==spaces['MC']==spaces['MR']=='X' or spaces['BL']==spaces['BC']==spaces['BR']=='X':
        print('Player 1 won!')
        return True
    elif spaces['TL']==spaces['ML']==spaces['BL']=='X' or spaces['TC']==spaces['MC']==spaces['BC']=='X' or spaces['TR']==spaces['MR']==spaces['BR']=='X':
        print('Player 1 won')
        return True
    elif spaces['TL']==spaces['MC']==spaces['BR']=='X' or spaces['TR']==spaces['MC']==spaces['BL']=='X':
        print('Player 1 won')
        return True

    # if there are 3 'O's on a line, finishes the game, displays winner
    if spaces['TL']==spaces['TC']==spaces['TR']=='O' or spaces['ML']==spaces['MC']==spaces['MR']=='O' or spaces['BL']==spaces['BC']==spaces['BR']=='O':
        print('Player 2 won')
        return True
    elif spaces['TL']==spaces['ML']==spaces['BL']=='O' or spaces['TC']==spaces['MC']==spaces['BC']=='O' or spaces['TR']==spaces['MR']==spaces['BR']=='O':
        print('Player 2 won')
        return True
    elif spaces['TL']==spaces['MC']==spaces['BR']=='O' or spaces['TR']==spaces['MC']==spaces['BL']=='O':
        print('Player 2 won')
        return True

    



while True:

    show_grid()

    # input from the 1st player
    p1_move = input('player 1, make your move pal: ').upper()
    if spaces[p1_move] == ' ':
        spaces[p1_move]=p1_shape
    else:
        continue

    show_grid()
    if end_of_game():
        break
    # if end_of_game()==True:
    #     break

    # input from the 2nd player
    p2_move = input('player 2, make your move please: ').upper()
    if spaces[p2_move] ==' ':
        spaces[p2_move]=p2_shape

    show_grid()
    if end_of_game():
        break
    # if end_of_game()==True:
    #     break

# 10.7.2022 -> write script of the game as written during school and developed solid bases of a tic tac toe game ran by python.
# 10.10 -> fix bugs of winner name being displayed twice.

# Challenge : write a program that allows 2 users to play tictactoe, displays winner and handles invalid input.
# Challenge completed! Well done JC:)