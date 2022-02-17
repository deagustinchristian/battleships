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
"""
Below function asks the player to enter a row and a column,
it checks so that the player enters a valid row number between 1-5 and a 
column letter A-E 
"""
    def get_player_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in "12345":
                print("Not a valid choice, please select a valid row")
                x_row = input("Enter the row of the ship: ")

            y_column = input("Enter the column letter of the ship: ").upper()
            while y_column not in "ABCDE":
                print("Not a valid choice, please select a valid column")
                y_column = input("Enter the column letter of the ship: ").upper()
            return int(x_row) - 1, Board.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_player_input()
    