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
        
        # Cuadrante 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        return num not in self.board[
            start_row:start_row+3,
            start_col:start_col+3
        ].flatten()
    
    def find_empty(self) -> Optional[Tuple[int, int]]:
        """Encuentra la próxima celda vacía (0)"""
        indices = np.where(self.board == 0)
        return (indices[0][0], indices[1][0]) if indices[0].size > 0 else None
    
    def solve(self, visualize: bool = False) -> bool:
        """Resuelve el sudoku usando backtracking"""
        empty = self.find_empty()
        
        if not empty:
            self.solution = self.board.copy()
            return True
            
        row, col = empty
        
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row, col] = num
                if visualize:
                    self.steps.append((row, col, num, True))
                
                if self.solve(visualize):
                    return True
                
                self.board[row, col] = 0
                if visualize:
                    self.steps.append((row, col, 0, False))
        
        return False
    
     def generate_puzzle(self, difficulty: int = 40) -> None:
        """Genera un nuevo puzzle de Sudoku"""
        # Tablero vacío
        self.board = np.zeros((9, 9), dtype=int)
        self.solve()
        
        # Remover números según dificultad
        to_remove = 81 - difficulty
        indices = np.random.choice(81, to_remove, replace=False)
        for idx in indices:
            row, col = divmod(idx, 9)
            self.board[row, col] = 0
        
        self.original = self.board.copy()
    
    def reset(self) -> None:
        """Reinicia al estado original"""
        self.board = self.original.copy()
        self.steps = []
        self.solution = None

if __name__ == "__main__":
    # Ejemplo de uso
    puzzle = [
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
    
    solver = SudokuSolver(puzzle)
    print("Puzzle original:")
    print(solver.board)
    
    start_time = time.time()
    solver.solve(visualize=True)
    print(f"\nSolución encontrada en {time.time() - start_time:.4f} segundos")
    print(solver.solution)