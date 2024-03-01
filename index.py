def start_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def make_player_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def play_game():
    board = start_board()
    display_board(board)
    player = "X"
    while True:
        row, col = make_player_move(player)
        if board[row][col] == " ":
            board[row][col] = player
            display_board(board)
            if check_winner(board, player):
                print(f"Player {player} wins!")
                break
            if all([cell != " " for row in board for cell in row]):
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")

play_game()
