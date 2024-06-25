
# Create a TicTacToe game in python, where two users can play together.
#Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
########################################################################
# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to get the position from the player
def player_input(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                return row, col
            else:
                print("Invalid input. Please enter values between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Function to check whether there is a winner or not
def check_win(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function to control the flow of the game
def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        display_board(board)
        row, col = player_input(current_player)
        
        # Check if the selected position is already taken
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Position already taken. Try again.")
            continue
        
        # Check for a win
        if check_win(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play()
