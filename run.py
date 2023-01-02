import math
import random
import time
import sys
from pprint import pprint
# animation for welcome title
from time import sleep 

# welcome title with aimation

welcome_title = "Welcome to the ultimate TIC TAC TOE Game!\n"

for x in welcome_title:
    print(x, end='')
    sys.stdout.flush()
    sleep(.1)

class Player:
    
    """  
      Initiates a player class. Each player in the game will be represented with an X or an O. 
      get_move function will allow all players to get their next move.
    """
    def __init__(self, letter):
        self.letter = letter
 
    def get_move(self, game):
        pass


class ComputerPlayer(Player): """ Specific kind of player that is going to be managed by the program."""
def __init__(self, letter):
        super().__init__(letter)
def get_move(self, game):
         """
        Computer will choose a random cell from the board.
        """
cell = random.choice(game.available_moves()) 
return cell


class HumanPlayer(Player):
    """
    Specific class for the human player.
    """
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
         """
        Check if the input value is one of the valid cells value,
        also checks if the cell on the board has already been used,
        if invalid or already used, will return an error.
        """
    valid_cell = None
    value = None
        while not valid_cell:
            cell = input(self.letter + "'s turn. Input move (0-8):")
            try:
                value = int(cell)
                if value not in game.available_moves():
                    raise ValueError
                valid_cell = True  # if no error found, then must be valid
            except ValueError:
                print("Invalid cell. Try again.")
        return value

class TicTacToe:
    """Class for the main game of Tic Tac Toe"""
def __init__(self):
        # single list that represents a 3x3 board, each number = cell
    self.board = [' ' for _ in range(9)]
        # keeps track of the winner if there is one
self.current_winner = None

def print_board(self):
        # group of three spaces are we choosing row1 = 0,1,2 \ row2 = 3,4,5 \ row3 = 6,7,8 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            # print a vertical line as a separator
            print("| " + " | ".join(row) + " |")

@staticmethod
def print_board_nums():
        """Show the number corrispondent to the cells and prints separators"""
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")


print(TicTacToe().print_board_nums())





