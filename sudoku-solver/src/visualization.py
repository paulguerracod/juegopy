import pygame
import numpy as np

class SudokuVisualizer:
    def __init__(self, solver):
        self.solver = solver
        pygame.init()
        self.width, self.height = 540, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Solver")
        
    def draw_grid(self):
        # Lógica para dibujar el tablero
        pass
    
    def animate_solution(self):
        # Animación paso a paso del proceso de solución
        for step in self.solver.steps:
            row, col, num, valid = step
            # Dibujar celda con color según validación
            # Actualizar pantalla
            pygame.time.delay(100)  # Control velocidad