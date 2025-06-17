import random


class BoardSpot:  # refactored the boardspot class to contain only essential data
    """
    represent a single cell on the minesweeper.
    """

    def __init__(self):
        """
        initializes the board spot with deafult values.
        """
        self.is_selected = False
        self.is_mine = False
        self.count = 0

    def __str__(self):
        """
        returns the string representation of the spot
        unselected cells show a blank, mines show '*',
        others show the mine count.
        """
        if not self.is_selected:
            return " "
        return "*" if self.is_mine else str(self.count)

    def is_mine_spot(self):
        """
        returns true if this spot contains a mine.
        """
        return self.is_mine


class Board:
    """
    representing the minesweeper game board and check values
    """

    def __init__(self, board_size, num_mines):
        """
        initializes the game board with the given size and number of mines
        This constructor creates a board grid (list of BoardSpot object) and randomly places mines
        in the grid
        """
        self.board_size = board_size
        self.num_mines = num_mines
        self.board = [[BoardSpot() for _ in range(board_size)] for _ in range(board_size)]
        self.selectable_spot = board_size * board_size - num_mines

        i = 0
        while i < num_mines:
            x = random.randint(0, board_size - 1)
            y = random.randint(0, board_size - 1)
            if not self.board[x][y].is_mine:
                self.add_mine(x, y)
                i += 1

    def __str__(self):
        """returns a string representation of the Minesweeeper board for display.
        the output string displayes the column and row indices with their respective board values
        str: A formatted string showing the Minesweeeper board layout
        """  # these tests ensure that __str__ displays the board correctly in various states
        display = " "  # when no cells are selected - when a safe cell is revealed - when a mine is revealed
        divider = "\n---"  # these tests help ensure the baord display matches the expected layout
        for i in range(self.board_size):
            display += "|{}".format(i)
            divider += "----"
        divider += "\n---"
        display += divider
        # Controlled board setups are used to verify expected output
        for y in range(self.board_size):
            display += str(y)
            for x in range(self.board_size):
                display += " | " + str(self.board[x][y])
            display += " |"
            display += divider
        return display  # returning the final string representation of the board

    def add_mine(self, x, y):
        """
        adds a mine to the spot (x, y) and increments the count of all adjacent cells
        """
        self.board[x][y].is_mine = True
        self.board[x][y].count = -1
        for i, j in self.get_neighbouring_coords_of(x, y):
            if not self.board[i][j].is_mine:
                self.board[i][j].count += 1

    def make_move(self, x, y):
        """
        reveals the selected celss. if it is a mine, then return False
        if it is a zero-count cell, recursively reveals adjacent cells
        after this;
        Returns:
             bool: False if a mine is hit, True otherwise.
        """
        spot = self.board[x][y]  # it returns False when selecting a mine,and True when revealing safe cells
        if spot.is_selected:  # Custom board setup will be used to control the test
            return True

        spot.is_selected = True
        self.selectable_spot -= 1

        if spot.is_mine:
            return False
        if spot.count == 0:
            for i, j in self.get_neighbouring_coords_of(x, y):
                if not self.board[i][j].is_selected:
                    self.make_move(i, j)
        return True

    def hit_mine(self, x, y):
        """
        returns True if the selected spot contains a mine
        """
        return self.board[x][y].is_mine

    def is_winner(self):
        """
        returns True if all non-mine spots have been selected.
        """
        return self.selectable_spot == 0

    def get_neighbouring_coords_of(self, x, y):
        """
        Gets all valid neighbouring coordinates around (x, y).
        Args:
            x (int): x-coordinates
            y (int): y-coordinates
        Returns:
            list of tuple: coordinates adjacent to (x,y)
        """
        coords = []
        for i in [x - 1, x, x + 1]:
            for j in [y - 1, y, y + 1]:
                in_range = 0 <= i < self.board_size and 0 <= j < self.board_size
                is_cell_itself = i == x and j == y
                if not is_cell_itself and in_range:
                    coords.append((i, j))
        return coords


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

