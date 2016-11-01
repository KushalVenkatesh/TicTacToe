# A TicTacToe Game for 2 Players
# Author: Jan Pascal Kunkler
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys

# define global variables for fields 1 - 9
c1, c2, c3, c4, c5, c6, c7, c8, c9 = range(1, 10)
board = [0, c1, c2, c3, c4, c5, c6, c7, c8, c9]

# function to clear entire terminal
clear_terminal = lambda : os.system('clear')

def start_game():
    choice = raw_input("Start game? (y/n): ")
    if 'y' in choice:
        clear_board()
        clear_terminal()
        matrix()
        player_one()
    else:
        sys.exit(0)

# show board/matrix
def matrix():
    print("\n")
    print(board[7], '|', board[8], '|', board[9])
    print('-'*9)
    print(board[4], '|', board[5], '|', board[6])
    print('-'*9)
    print(board[1], '|', board[2], '|', board[3])
    print("\n")

# Clear the board
def clear_board():
    global board
    board = [0, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# when game is over
def end(win, player):
    if not win:
        print("It's a tie!")
        start_game()

    else:
        print("Game Over!")
        print("Player {} wins!\n".format(player))
        start_game()

# error function
def error(code):
    if code == 0:
        print("Error: You can't use one field twice!!!\nGame over.")
        start_game()

    if code == 1:
        print("Error: Only input numbers from 1 to 9!\nGame over.")
        start_game()

# Check for all possible win conditions
def win(player):
    if ((board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or #row 1
    (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or
    (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or # row 2
    (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or
    (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or # row 3
    (board[7] == 'O' and board[8] == 'O' and board[9] == 'O') or
    (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or # column 1
    (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or
    (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or # column 2
    (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or
    (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or # column 3
    (board[3] == 'O' and board[6] == 'O' and board[9] == 'O') or
    (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or # diag L/R
    (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or
    (board[3] == 'X' and board[5] == 'X' and board[7] == 'X') or # diag R/L
    (board[3] == 'O' and board[5] == 'O' and board[7] == 'O')):
        victory = True
        end(victory, player)
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and
    board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and
    board[7] != ' ' and board[8] != ' ' and board[9] != ' '): # tied
        victory = False
        end(victory, player)
    else:
        return False


# do player move
def make_move(move, player):
    if player == 1 and board[move] == ' ': # only if position is empty
        board[move] = 'X'
    elif player == 2 and board[move] == ' ':
        board[move] = 'O'
    else:
        error(0) # if not empty, then throw duplicate error

    clear_terminal()
    matrix() # call matrix function to display current board

    # If game continues, switch to next player
    if not win(player):
        if player == 1:
            player_two()
        else:
            player_one()

def player_one():
    choice = int(raw_input("Player 1: "))
    if choice:
        make_move(choice, 1)

def player_two():
    choice = int(raw_input("Player 2: "))
    if choice:
        make_move(choice, 2)

def main():
    print("Welcome to this TicTacToe game for two!")
    print("Fields are numbered from left to right, 1 - 9")
    print("\nThis is your board:\n")
    matrix()
    print("\nPlayer 1 is X")
    print("Player 2 is O\n")

    start_game()


#-------------------------------------------------------


main()
