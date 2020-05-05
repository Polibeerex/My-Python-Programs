"""
Tic-tac-toe

The program is a simple version of the game.
In the class "Field" describes the events taking place on the playing field.
"""

from tabulate import tabulate
import random
import copy

# settings
player_is_first = True  # If "True" the player goes first
debug = False  # If "True" instead of empty cells, their numbers will be displayed
space = " "  # What will be shown in empty cells, if "debug" is "False"


class Field:
    """

    The basic logic of the game

    "__init__" method takes the value of the cell selected by the player;
    "adding" method adds an "X" to the selected cell and calls the "AI" method;
    "AI" method imitates the opponent’s move;
    "check" staticmethod checks if there is a winner:
        takes "key" string argument:
            if key is "win" the method returns True or False;
            if key is "who" the method returns who is winner;
    "show" staticmethod displays the game field;

    """
    if debug:
        cells: str = [["1", "2", "3"],
                      ["4", "5", "6"],
                      ["7", "8", "9"]]
    else:
        cells: str = [[space, space, space],
                      [space, space, space],
                      [space, space, space]]

    def __init__(self, cell):
        self.cell = cell
        self.row = 0
        self.col = 0
        self.option = copy.deepcopy(Field.cells)

        if self.cell in range(1, 4):
            self.row = 0
            if self.cell == 1:
                self.col = 0
            elif self.cell == 2:
                self.col = 1
            else:
                self.col = 2
        elif self.cell in range(4, 7):
            self.row = 1
            if self.cell == 4:
                self.col = 0
            elif self.cell == 5:
                self.col = 1
            else:
                self.col = 2
        else:
            self.row = 2
            if self.cell == 7:
                self.col = 0
            elif self.cell == 8:
                self.col = 1
            else:
                self.col = 2

    def adding(self, free: bool):

        if Field.cells[self.row][self.col] == space:
            Field.cells[self.row][self.col] = "X"
        else:
            print("This cell is already taken")
            free = False

        if not Field.check("win") and free:
            Field.AI(self)

    def AI(self):
        self.option[self.row][self.col] = "0"

        index_row = random.choice(range(len(self.option)))
        index_col = random.choice(range(len(self.option[index_row])))

        if self.option[index_row][index_col] != "0" and Field.cells[index_row][index_col] != "X" and \
                Field.cells[index_row][index_col] != "O":
            Field.cells[index_row][index_col] = "O"
        else:
            Field.AI(self)

    @staticmethod
    def check(key):
        win = False
        who = "Nobody"

        if Field.cells[0][0] == Field.cells[0][1] == Field.cells[0][2] and Field.cells[0][1] != space:
            win = True
            who = Field.cells[0][0]
        if Field.cells[1][0] == Field.cells[1][1] == Field.cells[1][2] and Field.cells[1][1] != space:
            win = True
            who = Field.cells[1][0]
        if Field.cells[2][0] == Field.cells[2][1] == Field.cells[2][2] and Field.cells[2][1] != space:
            win = True
            who = Field.cells[2][0]

        if Field.cells[0][0] == Field.cells[1][0] == Field.cells[2][0] and Field.cells[1][0] != space:
            win = True
            who = Field.cells[0][0]
        if Field.cells[0][1] == Field.cells[1][1] == Field.cells[2][1] and Field.cells[1][1] != space:
            win = True
            who = Field.cells[0][1]
        if Field.cells[0][2] == Field.cells[1][2] == Field.cells[2][2] and Field.cells[1][2] != space:
            win = True
            who = Field.cells[0][2]

        if Field.cells[0][0] == Field.cells[1][1] == Field.cells[2][2] and Field.cells[1][1] != space:
            win = True
            who = Field.cells[0][0]
        if Field.cells[0][2] == Field.cells[1][1] == Field.cells[2][0] and Field.cells[1][1] != space:
            win = True
            who = Field.cells[0][2]

        if key == "win":
            return win
        if key == "who":
            return who

    @staticmethod
    def show():
        print(tabulate(Field.cells, tablefmt="pretty"))


def ask():
    """Accepts and returns the cell selected by the player"""
    choise = int(input("Which cell do you want to choose?\n"))
    return choise


# who goes first
if not player_is_first:
    Field.AI(Field(None))

# show empty field
Field.show()


def run():
    """The function calls the necessary class methods in the desired sequence for the game to work correctly"""
    choise = ask()
    cell = Field(choise)
    Field.adding(cell, True)
    Field.show()


# The game will continue until someone wins or until empty cells run out
while not Field.check("win"):
    if any(space in cell for cell in Field.cells):
        run()
    else:
        print("Game over")
        break

# print who is winner
print(Field.check("who"), "is winner!")
