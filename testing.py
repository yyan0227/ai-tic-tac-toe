
import unittest
from tictactoe import player, actions, winner

X = "X"
O = "O"
EMPTY = None

class TestPlayer(unittest.TestCase):
    
    def test_initial_board(self):
        initial_board = [[EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY]]
        
        expected_output = X
        actual_output = player(initial_board)
        self.assertEqual(expected_output, actual_output)
    
    def test_O_turn(self):
        initial_board = [[EMPTY, EMPTY, EMPTY],
                         [EMPTY, X, EMPTY],
                         [EMPTY, EMPTY, EMPTY]]
        
        expected_output = O
        actual_output = player(initial_board)
        self.assertEqual(expected_output, actual_output)
    
    def test_X_turn(self):
        initial_board = [[EMPTY, EMPTY, O],
                         [EMPTY, X, EMPTY],
                         [EMPTY, EMPTY, EMPTY]]
        
        expected_output = X
        actual_output = player(initial_board)
        self.assertEqual(expected_output, actual_output)


class TestActions(unittest.TestCase):

    def test_initial_board(self):
        initial_board = [[EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY]]
        
        expected_output = set()
        for row in range(len(initial_board)):
            for col in range(len(initial_board[row])):
                expected_output.add((row, col))
        
        actual_output = actions(initial_board)

        self.assertSetEqual(expected_output, actual_output)
    
    def test_actions_1(self):
        initial_board = [[X, EMPTY, EMPTY],
                         [EMPTY, O, EMPTY],
                         [EMPTY, EMPTY, O]]
        
        expected_output = {(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)}
        actual_output = actions(initial_board)

        self.assertSetEqual(expected_output, actual_output)


class TestWinner(unittest.TestCase):

    def test_initial_board(self):
        initial_board = [[EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY]]
        
        # no winner
        actual_output = winner(initial_board)
        self.assertIsNone(actual_output)
    
    def test_horizontal_winner(self):
        initial_board = [[X, O, O],
                         [X, X, X],
                         [O, X, O]]
        
        expected_output = X
        actual_output = winner(initial_board)
        self.assertEqual(expected_output, actual_output)
    
    def test_vertical_winner(self):
        initial_board = [[O, X, O],
                         [X, X, O],
                         [X, O, O]]
        
        expected_output = O
        actual_output = winner(initial_board)
        self.assertEqual(expected_output, actual_output)
    
    def test_diagonal_winner_1(self):
        initial_board = [[O, X, O],
                         [X, O, X],
                         [X, O, O]]
        
        expected_output = O
        actual_output = winner(initial_board)
        self.assertEqual(expected_output, actual_output)
    
    def test_diagonal_winner_2(self):
        initial_board = [[O, O, X],
                         [X, X, O],
                         [X, O, O]]
        
        expected_output = X
        actual_output = winner(initial_board)
        self.assertEqual(expected_output, actual_output)
    
    def test_no_winner(self):
        initial_board = [[O, X, X],
                         [X, O, O],
                         [X, O, X]]
        
        actual_output = winner(initial_board)
        self.assertIsNone(actual_output)


if __name__ == "__main__":
    unittest.main()
