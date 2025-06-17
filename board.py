""" Copyright Oxford Brookes University
Student Number: 19334208 """

import random
from board_spot import BoardSpot

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
        self.add_mine(x,y)
        i += 1
  def __str__(self):
    """returns a string representation of the Minesweeeper board for display.
    the output string displayes the column and row indices with their respective board values
    str: A formatted string showing the Minesweeeper board layout
    """ #these tests ensure that __str__ displays the board correctly in various states
    display = " "    # when no cells are selected - when a safe cell is revealed - when a mine is revealed
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
    return display # returning the final string representation of the board
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
    spot = self.board[x][y] # it returns False when selecting a mine,and True when revealing safe cells
    if spot.is_selected:    # Custom board setup will be used to control the test
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