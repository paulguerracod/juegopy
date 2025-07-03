import sys
import os
import unittest

# Agrega el directorio src al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sudoku_solver import SudokuSolver  # Importación relativa corregida

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
        self.assertIsNotNone(self.solver.solution)
        self.assertFalse(0 in self.solver.solution.flatten())
    
    def test_valid_move(self):
        self.assertTrue(self.solver.is_valid(0, 2, 4))
        self.assertFalse(self.solver.is_valid(0, 2, 5))
        self.assertFalse(self.solver.is_valid(0, 2, 3))

if __name__ == '__main__':
    unittest.main()