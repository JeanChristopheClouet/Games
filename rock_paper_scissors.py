import random


ALLOWED = ['R','P','S']

while True:
    name = input('> Player name: ')
    pandm = {}
    player = input('> Your move: ')
    if player not in ALLOWED:
        print('> Please enter valid move')
        continue

    #print(player) # ptit debug
    pandm[player] = name # assigning key, value = name, move to pandm
   

    bot = 'bot'
    ia = None
    num = random.randint(0,2)
    if num == 0 :
        ia = 'R'
    elif num == 1:
        ia = 'P'
    else:
        ia = 'S'
    bandm = {}
    print(bandm)
    bandm[ia] = bot

    print(pandm)
    print(bandm) # ptit debug

    players = player, ia

    
    if player == ia:
        print(f'It\'s a tie')
    elif player == 'R' and ia == 'S':
        print(f'{pandm[player]} wins.')
    elif player == 'S' and ia == 'P':
        print(f'{pandm[player]} wins.')
    elif player == 'P' and ia == 'R':
        print(f'{pandm[player]} wins.')
    else:
        print(f'{bandm[ia]} wins.')
 
    print('*' * 80)

    keepPlaying = input('Keep playing?(y/n): ')
    if keepPlaying == 'n':
        quit()

# (*^-^*)