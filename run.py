from random import randint

import os

class Board:
    def __init__(self, board):
        self.board = board
"""
Below function converts numbers to letters when displaying the columns
"""
    def get_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    def print_board(self):
        print("  A B C D E")
        row_number = 1
        for row in self.board:
            print("row_number, ".".join(row))")
            row_number += 1

class Ships:
    def __init__(self, board):
        self.board = board
"""
Below function places 6 ships randomly on the board and checks 
if there is already a ship placed, 
if so it continues to look until it finds a free spot
"""
    def create_ships(self):
        for i in range(6):
            self.x_row, self.y_column = random.randint(0, 4), random.randint(0, 4)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 4), random.randint(0, 4)
            self.board[self.x_row][self.y_column] = "X"
        return self.board