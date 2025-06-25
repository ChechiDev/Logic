import os
import random

"""
FLOOD FILL ALGORITHM
"""

ROWS = 6
COLUMNS = 7

class Logic:
    def __init__(self, row, col):
        self.board = []
        self.row = row
        self.col = col
        self.empty = "."
        self.piece = "X"


    def create_board(self):
        self.board = [[self.empty] * self.col for _ in range(self.row)]

        for r in self.board:
            print("  ".join(r))


    def print_board(self):

        for row in self.board:
            print("  ".join(row))


    def insert_piece(self, col):
        # Buscar desde la última fila hacia arriba
        for x in range(len(self.board)-1, -1, -1):
            if self.board[x][col] == self.empty:
                self.board[x][col] = self.piece

                self.print_board()
                print(f"Pieza insertada en fila {x}, columna {col}.")
                return

        print("La columna está llena.")




















if __name__ == "__main__":
    ff = Logic(row=ROWS, col=COLUMNS)
    ff.create_board()

    while True:
        # ff.print_board()
        col = int(input("Columna donde insertar la pieza (o -1 para salir): "))
        if col == -1:
            break
        ff.insert_piece(col)
