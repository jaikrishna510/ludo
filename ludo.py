import random

# Initialize the board
board = ['-' for _ in range(52)]
tokens = {'A': [0, 0, '-'], 'B': [0, 0, '-']}

# Function to display the board
def display_board():
    print(' '.join(board[:6]))
    print(' '.join(board[11:5:-1]) + ' ' + ' '.join(board[6:12]))
    print(' '.join(board[12:18]))
    print(' '.join(board[23:17:-1]) + ' ' + ' '.join(board[18:24]))
    print(' '.join(board[24:30]))
    print(' '.join(board[35:29:-1]) + ' ' + ' '.join(board[30:36]))
    print(' '.join(board[36:42]))
    print(' '.join(board[47:41:-1]) + ' ' + ' '.join(board[42:48]))
    print(' '.join(board[48:]))

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to move the token
def move_token(player):
    roll = roll_dice()
    print(f"Player {player}'s turn. Rolled a {roll}.")
    
    if tokens[player][2] == '-':
        if roll == 6:
            tokens[player][2] = 0
            board[1] = player
        else:
            print("No token on the board. Try again next turn.")
    else:
        current_pos = tokens[player][2]
        new_pos = current_pos + roll
        
        if new_pos > 51:
            print("Cannot move token. Try again next turn.")
        elif new_pos == 51:
            tokens[player] = [0, 0, '-']
            board[current_pos] = '-'
            board[new_pos] = player
            display_board()
            print(f"Player {player} wins!")
            return True
        else:
            tokens[player][2] = new_pos
            board[current_pos] = '-'
            if board[new_pos] != '-':
                print(f"Token of Player {board[new_pos]} knocked off!")
                tokens[board[new_pos]] = [0, 0, '-']
            board[new_pos] = player
            display_board()

    return False

# Main game loop
def play_ludo():
    display_board()
    winner = False
    players = ['A', 'B']
    turn = 0

    while not winner:
        player = players[turn]
        winner = move_token(player)
        turn = (turn + 1) % 2

# Start the game
play_ludo()
