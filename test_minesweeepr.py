""" Copyright Oxford Brookes University
Student Number: 19334208 """
import unittest
from board import Board


class TestBoard(unittest.TestCase):
    """Unit tests for the Board class in the Minesweeeper game."""

    def test_add_mine(self):
        """test that a mine is coorectly added and neighbour's counts are incremented."""
        board = Board(10, 0)
        board.add_mine(5, 5)
        self.assertEqual(board.board[5][5].count, -1)
        self.assertEqual(board.board[4][4].count, 1)
        self.assertEqual(board.board[6][6].count, 1)

    def test_get_neighbouring_coords_of(self):
        """Test the coorectly neighbouring coordinates are returned for given position"""
        board = Board(3, 0)
        self.assertEqual(board.get_neighbouring_coords_of(1, 1),
                         [(0, 0), (0, 1), (0, 2),
                          (1, 0), (1, 2),
                          (2, 0), (2, 1), (2, 2)])
        self.assertEqual(board.get_neighbouring_coords_of(0, 0),
                         [(0, 1), (1, 0), (1, 1)])

    def test_make_move_hits_mine(self):
        """test that making a move on a mine returns False (basically game over)."""
        board = Board(3, 0)
        board.board[1][1].is_mine = True
        board.board[1][1].count = -1
        self.assertFalse(board.make_move(1, 1))

    def test_make_move_clears_center(self):
        """tests that making a move on a zero-count cell reveals adjacent cells recursively"""
        board = Board(5, 0)
        board.board[2][2].count = 0
        board.make_move(2, 2)
        self.assertTrue(board.board[2][2].is_selected)
        for x, y in board.get_neighbouring_coords_of(2, 2):
            self.assertTrue(board.board[x][y].is_selected)

    def test_str_empty_board(self):
        """
        test the  string representation of an empty board contains expected elements
        """
        game = Board(2, 0)
        board_output = str(game)
        self.assertIn("|", board_output)
        self.assertIn("0", board_output)

    def test_str_after_move(self):
        """test that the coorect number is displayed after a move is made."""
        game = Board(2, 0)
        game.board[0][0].count = 1
        game.board[0][0].is_selected = True
        output = str(game)
        self.assertIn("1", output)

    def test_str_after_mine_selected(self):
        """test that a selected mine is displayed as "*" on the board."""
        game = Board(2, 0)
        game.board[1][1].is_mine = True
        game.board[1][1].count = -1
        game.board[1][1].is_selected = True
        output = str(game)
        self.assertIn("*", output)


if __name__ == "__main__":
    unittest.main()
