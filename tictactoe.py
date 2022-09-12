# Author: Justin Scott

from board import *
from helpers import *


# Driver code that plays the game
def play_game():
    # The opposite player starts first because of the timing of switching players.
    player = 'O'

    # Amount of moves that have happened. Used to determine if it's a draw.
    moves = 0

    # Draws the board format. [0] is None to eliminate confusion with indices in formatting.
    draw_board([None, '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    reset_board()

    while not is_win(get_board()):

        # Draws the current board
        draw_board(get_board())

        # If the board is full, it's a draw
        if moves == 9:
            print('It\'s a draw!')
            break

        # Switch players
        player = switch_players(player)

        # Ask current player to make their move
        ask(player)

        # Keep asking to make a new move until a legal move is made
        while not make_move(player, get_user_move()):
            ask(player)
            draw_board(get_board())

        moves += 1

    if is_win(get_board()):
        print(f'Player {player} wins!')

    if play_again(input('Would you like to play again?')):
        play_game()


play_game()
