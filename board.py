# Author: Justin Scott

# Blank board
board_values = [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Draws the given board
# @param values: List of the board needed to be drawn
def draw_board(values):
    print('\n')
    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(values[1], values[2], values[3]))
    print('\t_____|_____|_____')

    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(values[4], values[5], values[6]))
    print('\t_____|_____|_____')

    print('\t     |     |')

    print('\t  {}  |  {}  |  {}'.format(values[7], values[8], values[9]))
    print('\t     |     |')
    print('\n')


# Wipes the board to its default values. Leaves the None at [0] alone.
def reset_board():
    for i in range(1, len(board_values)):
        board_values[i] = ' '


# Sets the board value to 'X' or 'O' depending on the player
# @param player: The player making the move
# @param position: Where on the board the move is being made
def make_move(player, position):
    # Checks to make sure the move is in bounds.
    if position < 1 or position > 9:
        print('Illegal move: Position is out of bounds. Try again.')
        draw_board(get_board())
        return False
    # Checks to make sure the move is being made in an empty spot.
    if board_values[position] != ' ':
        print('Illegal move: Position is already taken. Try again.')
        draw_board(get_board())
        return False
    if player == 'X':
        board_values[position] = 'X'
        return True
    elif player == 'O':
        board_values[position] = 'O'
        return True


# Logic for if the current board has a win for either player
# @param board: The current board values
def is_win(board):
    if (board[1] == board[2] == board[3] and board[1] != ' ') or (
            board[4] == board[5] == board[6] and board[4] != ' ') or (
            board[7] == board[8] == board[9] and board[7] != ' ') or (
            board[1] == board[5] == board[9] and board[1] != ' ') or (
            board[3] == board[5] == board[7] and board[3] != ' ') or (
            board[1] == board[4] == board[7] and board[1] != ' ') or (
            board[2] == board[5] == board[8] and board[2] != ' ') or (
            board[3] == board[6] == board[9] and board[3] != ' '):
        draw_board(get_board())
        return True
    return False


# Returns the board values
def get_board():
    return board_values
