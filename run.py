"""importing modules"""
import math
import random
import time
import os


class Player:
    """
    Initiates a player class.
    Each player in the game will be represented with X or O.
    get_move function will allow all players to get their next move.
    """
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class ComputerPlayer(Player):
    """
    Player that is going to be managed by the program.
    """
    def get_move(self, game):
        """
        Computer choose random cell.
        """
        cell = random.choice(game.available_moves())
        return cell


class HumanPlayer(Player):
    """
    Class for the human player.
    """
    def get_move(self, game):
        """
        Checks if the input is valid value.
        """
        valid_cell = None
        value = None
        while not valid_cell:
            cell = input(self.letter + "'s turn. Input move (0-8):\n")
            try:
                value = int(cell)
                if value not in game.available_moves():
                    raise ValueError
                valid_cell = True  # if no error found -> then must be valid
            except ValueError:
                print("Invalid cell. Try again numbers from 0-8.")
        return value


def mockup_board():
    """
    Board to keep visible during the game for easier understanding.
    """
    num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in num_board:
        print("| " + " | ".join(row) + " |")


class TicTacToe:
    """
    Class defines the game
    """
    def __init__(self):
        """
        Single list that represents a 3x3 board, each number = cell
        and keeps track of the winner if there is one.
        """
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        """
        Group of three spaces row1 = 0,1,2 / row2 = 3,4,5 / row3 = 6,7,8
        and print a vertical line as a separator
        """
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        """
        Show the number corrispondent to the cells and prints separators
        """
        print('')
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        """
        Defines which moves are still available in a list of indeces
        """
        moves = []
        for (i, cell) in enumerate(self.board):
            if cell == " ":
                moves.append(i)
        return moves

    def empty_cells(self):
        """
        Returns True if there are empty cells in the board.
         """
        return " " in self.board

    def num_empty_cells(self):
        """
        Count how many empty cells are in the baord
        """
        return self.board.count(" ")

    def make_move(self, cell, letter):
        """
        If the move is valid, then make the move and assign cell to letter
        then return True. If not valid, return False.
        Function also checks for the winner after player has made a move.
        """
        if self.board[cell] == " ":
            self.board[cell] = letter
            if self.winner(cell, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, cell, letter):
        """
        Check if there is a winner.
        Checks for 3 in a row, column or diagonal.
        """
        # checks rows first
        row_index = math.floor(cell / 3)
        row = self.board[row_index*3: (row_index + 1)*3]
        # If all this is true or else comes out as false
        # check if that letter is in 3 spots in a row
        if all([spot == letter for spot in row]):
            return True

        # If not true then we keep going
        # check columns
        col_index = cell % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # checks only if cell is an even number (0, 2, 4, 6, 8)
        if cell % 2 == 0:  # if it's even
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all this checks fail then there is no possible winner
        return False


def clear_screen(numlines=100):
    """
    Clears the screen to simplify UX and clear visual clutter.
    numlines is an optional argument used only as a fall-back.
    """
    if os.name == "posix":
        # for OS => Unix / Linux / MacOS / BSD / etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        #  for OS => DOS / Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)


def play(game, x_player, o_player, print_game=True):
    """
    Main function to play the game.
    Iterate while the game has empty cells.
    When winner is returned, breaks the loop.
    Returns the winner if there is one or None for a tie.
    """
    if print_game:
        print('')
        print("To select one of the cells:")
        print("Type the number in the spot of your choice!")
        print('')
        print("Reference board:")
        game.print_board_nums()
        print('')

    letter = "X"  # starting letter

    while game.empty_cells():
        # get the move from the correct player
        if letter == "O":
            cell = o_player.get_move(game)
        else:
            cell = x_player.get_move(game)

        # make a move
        if game.make_move(cell, letter):
            if print_game:
                print('')
                print('')
                print(f"{letter} makes a move to cell {cell}")
                game.print_board()
                print("")  # empty line to separate
                print("Reference board:")
                mockup_board()
                print("")  # empty line to separate

            if game.current_winner:
                if print_game:
                    print(letter + " wins! \n")
                    print('')
                return letter  # returns the winner

            # after the move, alternate letters
            if letter == "X":
                letter = "O"
            else:
                letter = "X"

        # add pause to allow user to read computer moves
        time.sleep(0.8)

    if print_game:
        print("It's a draw!")
        return None


def explain_game():
    print("")
    print("Tic-tac-toe is a game in which two players take turns in drawing")
    print("either an 'O' or an 'X' in one square of a grid")
    print("consisting of nine squares.")
    print("The winner is the first player to get three of the same symbols")
    print("in a row, vertically, horizontally or diagonally.")
    print("")
    print("Now press 'p' to play or 'q' to quit the game!")


def start_the_game():
    """
    Gives the user menu for info, start the game or quit.
    """
    x_player = HumanPlayer("X")
    o_player = ComputerPlayer("O")
    t = TicTacToe()
    print('')
    print("You have the X symbol assigned to you to play,")
    print("while the computer has the symbol O")
    print('')
    print("To continue, select a command with one of the following:")
    print("Press 'p' to play the game")
    print("Press 'r' to read the rules")
    print("Press 'q' To quit the game")
    while True:
        user_choice = input().strip().lower()
        if user_choice == 'r':
            clear_screen()
            explain_game()
        elif user_choice == 'p':
            clear_screen()
            play(t, x_player, o_player, print_game=True)
            return
        elif user_choice == 'q':
            clear_screen()
            print('')
            print("Thank you for playing!")
            print('')
            break
        else:
            print("Wrong input. Press 'p' to play or 'r' to read the rules.")


def main():
    """
    Main function that calls the start and end of game.
    """
    clear_screen()
    print('')
    print("Welcome to ultimate Tic Tac Toe!")
    print("Please enter your name:")
    name = input()
    print("------------------")
    print('')
    print(f"Welcome {name}!")
    print('')
    print("Would you like to play Tic Tac Toe?")
    print("Enter 'y' for YES or 'n' for NO:")
    user_choice = input().strip().lower()
    if user_choice == 'y':
        clear_screen()
        start_the_game()
        while True:
            print("Would you like to play again?")
            print("Enter 'y' for YES or 'n' for NO:")
            user_choice = input().strip().lower()
            if user_choice == 'y':
                clear_screen()
                start_the_game()
            elif user_choice == 'n':
                clear_screen()
                print("Thank you for playing!")
                break
            else:
                print("Invalid command. Press 'y' to start and 'n' to quit.")
    elif user_choice == 'n':
        clear_screen()
        print("Thank you for playing!")
        print("To restart the game:")
        print("press Run program above the terminal window.")
    else:
        print("Invalid command. Press 'y' to start and 'n' to quit.")


if __name__ == '__main__':
    while True:
        main()
