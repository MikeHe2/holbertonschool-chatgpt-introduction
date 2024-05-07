def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Expanded to match the size of the board when using 3 columns

def check_winner(board):
    # Check horizontal, vertical, and diagonal lines
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0  # Track the number of moves to determine if the board is full

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in range(3) or col not in range(3):
                print("Invalid indices, please enter 0, 1, or 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        board[row][col] = player
        moves += 1
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if moves == 9:
            print_board(board)
            print("The game is a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

