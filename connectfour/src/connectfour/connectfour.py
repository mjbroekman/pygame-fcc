import numpy as np
import math
#import pygame
import sys

def create_board(rows, cols):
    return np.zeros((rows,cols), int)

def is_valid_place(board,column):
    if 0 not in board[:,column]:
        return False
    return True

def place_piece(board,player,column):
    _tmp = np.where(np.flipud(board)[:,column] == 0)[0][0]
    row = len(board[:,column]) - _tmp - 1
    board[:,column][row] = player
    # print(board[:,column])
    return board

def is_game_over(board:np.ndarray):
    _p1_seq = list([1]) * 4
    _p2_seq = list([2]) * 4

    # For row or column wins, this is easy.
    # Simply iterate over the rows, rotate the matrix, iterate again
    for layout in board, np.rot90(board):
        row_count = len(layout)
        for row in range(0,row_count):
            row_arr = list(layout[row])
            for i in range(0,(len(row_arr) - 3)):
                if row_arr[i:i+4] == _p1_seq:
                    print("Player 1 WINS!")
                    return True

                if row_arr[i:i+4] == _p2_seq:
                    print("Player 2 WINS!")
                    return True
        
        # At the same time, we can take the length of the row div2
        # Then check all the diagonals from -div to +div!!!
        for diagonal in range(-row_count // 2,row_count // 2):
            diag = np.diag(layout,diagonal)
            row_arr = list(diag)
            if len(row_arr) >= 4:
                for i in range(0,(len(row_arr) - 3)):
                    if row_arr[i:i+4] == _p1_seq:
                        print("Player 1 WINS ON A DIAGONAL!")
                        return True

                    if row_arr[i:i+4] == _p2_seq:
                        print("Player 2 WINS ON A DIAGONAL!")
                        return True

    return False

board = create_board(6,7)
player_turn = 1
print(board)

while not is_game_over(board):
    col_choice = -1
    while col_choice < 0 or col_choice > 6:
        try:
            col_choice = int(input(f"Player {player_turn}, place your piece in a column [0-6]: "))
        except ValueError:
            col_choice = -1
        except KeyboardInterrupt:
            sys.exit()

    if is_valid_place(board,col_choice):
        board = place_piece(board,player_turn,col_choice)
        # The selected column was not full, save the piece and switch players...
        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1

    else:
        print("That column is full, pick another column")

    print(board)