import unittest
from src.sudoku_solver import SudokuSolver

class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self.puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.solver = SudokuSolver(self.puzzle)
    
    def test_solution(self):
        self.assertTrue(self.solver.solve())
        self.assertFalse(0 in self.solver.solution)
    
    def test_valid_move(self):
        self.assertTrue(self.solver.is_valid(0, 2, 4))
        self.assertFalse(self.solver.is_valid(0, 2, 5))

if __name__ == '__main__':
    unittest.main()