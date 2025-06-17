""" Copyright Oxford Brookes University
Student Number: 19334208 """

from board import Board


def get_valid_board_size():
    """
    Promt user for a valid board size between 3 and 20.
    """
    while True:
        try:
            size = int(input("Choose the width of the board (between 3 and 20): ".format()))
            if 3 <= size <= 20:
                return size
            else:
                print("Invalid board size. Please choose between 3 and 20. ")
        except ValueError:
            print("Invalid input. Please enter a number. ")


def get_valid_mine_count(board_size):
    """
    prompts user for a valid number of mines based on board size.
    """
    max_mines = board_size * board_size - 1
    while True:
        try:
            mines = int(input("Choose the number of mines (1 to {}): ".format(max_mines)))
            if 1 <= mines < board_size * board_size:
                return mines
            else:
                print("Invalid number. Please choose between 1 and {}.".format(max_mines))
        except ValueError:
            print("Invalid input. Please enter a number")


def get_valid_move(board, board_size):
    """
    prompts user for a valid move that is within board range
    and not already selected.
    """
    while True:
        try:
            x = int(input("x: "))
            y = int(input("y: "))
            if 0 <= x < board_size and 0 <= y < board_size:
                if not board.board[x][y].is_selected:
                    return x, y
                else:
                    print("This cell is already selected. Try another one.")
            else:
                print("Coordinates out of range.")
        except ValueError:
            print("Invalid input. Please enter integers.")


def play_game():
    """
    runs the main game loop.
    """
    board_size = get_valid_board_size()
    num_mines = get_valid_mine_count(board_size)
    game_board = Board(board_size, num_mines)

    game_over = False
    winner = False

    while not game_over:
        print(game_board)
        print("Make your move: ")
        x, y = get_valid_move(game_board, board_size)
        if not game_board.make_move(x, y):
            game_over = True
        elif game_board.is_winner():
            game_over = True
            winner = True

    print(game_board)
    if winner:
        print("Congratulations, You Win!")
    else:
        print("You hit a mine. Game Over!")


if __name__ == "__main__":
    play_game()
