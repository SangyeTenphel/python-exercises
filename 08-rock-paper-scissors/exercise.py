while True:
    player1 = input('\nPlayer1: rock, paper or scissors? ')
    player2 = input('Player2: rock, paper or scissors? ')

    if player1 == player2:
        print('Tie!')
    elif player1 == 'rock':
        if player2 == 'paper':
            print('Player2 wins!',player2,'covers',player1)
        else:
            print('Player1 wins!',player1,'smashes',player2)
    elif player1 == 'paper':
        if player2 == 'scissors':
            print('player2 wins!',player2,'cuts',player1)
        else:
            print('Player1 wins!',player1,'covers',player2)
    elif player1 == 'scissors':
        if player2 == 'rock':
            print('Player2 wins!',player2,'smashes',player1)
        else:
            print('Player1 wins!',player1,'cuts',player2)
    else:
        print('That is not a valid play. Check your spelling!')
       
    choice = input('\nDo you want to play again(y/n)?')
    if choice == 'n':
        break
print('\nThanks for playing!')

