""" Copyright Oxford Brookes University
Student Number: 19334208 """

class BoardSpot: #refactored the boardspot class to contain only essential data
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