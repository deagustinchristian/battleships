import random
import os


class Board:
    def __init__(self, board):
        self.board = board

# Below function converts numbers to letters when displaying the columns

    def get_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    # Part of this code I got from dmoisset, see README
    def print_board(self):
        print("  A B C D E")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Ships:
    def __init__(self, board):
        self.board = board
    """
    Below function places the computers 6 ships
    randomly on the board and checks
    if there is already a ship placed,
    if so it continues to look until it finds a free spot
    """
    def create_ships(self):
        for i in range(6):
            self.x_row, self.y_column = (random.randint(0, 4),
                                         random.randint(0, 4))
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = (random.randint(0, 4),
                                             random.randint(0, 4))
            self.board[self.x_row][self.y_column] = "X"
        return self.board
    """
    Below function asks the player to enter a row and a column,
    it checks so that the player enters a valid row number between 1-5 and a
    column letter A-E
    """
    # fix input validation, blank input!!!
    # restrict to one character/number test abcde 12345
    def get_player_input(self):
        try:
            x_row = input("Enter the row of the ship: \n")
            while x_row not in "12345":
                print("Not a valid choice, please choose 1, 2, 3, 4, or 5")
                x_row = input("Enter the row of the ship: \n")
            # .upper makes it possible to allow
            # player to input lower case letters, a-e
            y_column = input("Enter the column letter of the ship: \n").upper()
            while y_column not in "ABCDE":
                print("Not a valid choice, please choose A, B, C, D, or E")
                y_column = (input("Enter the column
                                  letter of the ship: \n").upper())
            return int(x_row) - 1, Board.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_player_input()

    def sunk_ships(self):
        sunk_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    sunk_ships += 1
        return sunk_ships


def new_game():
    computer_board = Board([[" "] * 5 for i in range(5)])
    player_guess_board = Board([[" "] * 5 for i in range(5)])
    Ships.create_ships(computer_board)

    missiles = 15
    num_ships = 6
    print("≈" * 50)
    print("Welcome to Battleships!")
    print((f"Amount of missiles: {missiles}.
          Number of enemy ships: {num_ships}"))
    print("Happy hunting!")
    print("≈" * 50)

    while missiles > 0:
        Board.print_board(player_guess_board)

    # Gets the player input and checks so not duplicate
        player_x_row, player_y_column = Ships.get_player_input(object)

        while player_guess_board.board[player_x_row][player_y_column] == "-" or player_guess_board.board[player_x_row][player_y_column] == "X":
            print("You tried this one already!")
            player_x_row, player_y_column = Ships.get_player_input(object)

    # checks if its a hit or a miss
        if computer_board.board[player_x_row][player_y_column] == "X":
            print("You sunk one of my battleships!")
            player_guess_board.board[player_x_row][player_y_column] = "X"
        else:
            print("You missed!")
            player_guess_board.board[player_x_row][player_y_column] = "-"

        if Ships.sunk_ships(player_guess_board) == 6:
            print("You sunk all 6 battleships! You won the game!")
            break
        else:
            missiles -= 1
            print(f"You have {missiles} missiles left")
            if missiles == 0:
                print("You ran out of missiles, the bad guys got away!")
                Board.print_board(player_guess_board)
                break


new_game()