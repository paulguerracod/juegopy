import numpy as np
import time
from typing import List, Optional, Tuple

class SudokuSolver:
    def __init__(self, board: List[List[int]]):
        self.board = np.array(board)
        self.original = np.array(board)
        self.steps = []
        self.solution = None
        
    def is_valid(self, row: int, col: int, num: int) -> bool:
        """Verifica si un número es válido en una posición"""
        # Fila y columna
        if num in self.board[row, :] or num in self.board[:, col]:
            return False