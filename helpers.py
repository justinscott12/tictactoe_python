# Author: Justin Scott

# These are just helper methods that make the driver code simpler

# Asks the current player to make a move
# @param player: The current player
def ask(player):
    print(f'Player {player}\'s turn:')


# Switches the player that has to make a move
# @param player: The current player
def switch_players(player):
    if player == 'X':
        return 'O'
    return 'X'


# Retrieves user's move, must be an int
def get_user_move():
    return int(input())


# Asks the player if they want to play again
# @param user_input: the user input if they want to play again or not
def play_again(user_input):
    if user_input.upper() == 'T' or user_input.upper() == 'TRUE' or user_input.upper() == 'Y' or user_input.upper() == 'YES':
        return True
    return False
