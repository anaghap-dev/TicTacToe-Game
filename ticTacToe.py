import random


def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")


def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_draw(board):
    return all([spot != " " for spot in board])


def computer_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(available_moves)


def play_game():
    print("\n-------------------------------------------------------------------------------------------------------")
    print("                                              Tic Tac Toe")
    print("-------------------------------------------------------------------------------------------------------")
    board = [" " for _ in range(9)]
    current_player = "X"

    game_mode = input(
        "Do you want to play with: \n1 - Your friend \n2 - The Computer\nEnter your choice: ")

    while game_mode not in ["1", "2"]:
        game_mode = input(
            "Invalid input. Please enter 1 for friend or 2 for computer: ")

    if game_mode == "2":
        user_choice = input("Do you want to be X or O? ").upper()
        while user_choice not in ["X", "O"]:
            user_choice = input(
                "Invalid choice. Please select X or O: ").upper()

        if user_choice == "X":
            user = "X"
            computer = "O"
        else:
            user = "O"
            computer = "X"

    while True:
        print_board(board)

        if game_mode == "1" or current_player == user:
            print(f"Player {current_player}'s turn.")
            try:
                move = int(input(f"Choose your move (1-9): ")) - 1
                if board[move] != " ":
                    print("That spot is already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please choose a number between 1 and 9.")
                continue
        else:
            print("Computer's turn.")
            move = computer_move(board)

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            if game_mode == "1":
                print(f"Player {current_player} wins!")
            else:
                if current_player == user:
                    print("You win!")
                else:
                    print("Computer wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


play_game()
