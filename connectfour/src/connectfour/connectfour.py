import numpy as np
import math
import pygame
import sys
import argparse

def create_board(rows, cols, size, gui):
    screen = None
    if gui:
        total_height = ( rows * size ) + size
        total_width = cols * size
        screen =  pygame.display.set_mode((total_width,total_height))

    return (np.zeros((rows,cols), int),screen)

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

def draw_board(board,gui_board,size):
    print(board)
    if gui_board is not None:
        for column in range(gui_board.get_width() // size):
            for row in range(gui_board.get_height() // size):
                if row == 0:
                    pygame.draw.rect(gui_board,(0,0,0),(column*size,row*size,size,size))
                else:
                    pygame.draw.rect(gui_board,(0,0,255),(column*size,row*size,size,size))
        
        pygame.display.update()
        pass



# Defaults
rows = 6
cols = 7
size = 100
gui = False
debug = 0

if __name__ == '__main__':
    # Use argparse to read command-line arguments to create the board...
    import argparse
    parser = argparse.ArgumentParser(description="A game of ConnectFour implemented in Python.")
    parser.add_argument("--rows",action="store",type=int,help="Number of rows",default=6)
    parser.add_argument("--cols",action="store",type=int,help="Number of columns",default=7)
    parser.add_argument("--size",action="store",type=int,help="Width of each column", default=100)
    parser.add_argument("--gui",action="store_true",help="Show a PyGame GUI instead of CLI")
    parser.add_argument("--debug","-d",action="count",help="Set debug level. Can be used multiple times to increase debug level",default=0)
    args = parser.parse_args()

    rows = args.rows
    cols = args.cols
    size = args.size
    gui = args.gui
    debug = args.debug


pygame.init()

(board,gui_board) = create_board(rows,cols,size,gui)
player_turn = 1
draw_board(board,gui_board,size)

while not is_game_over(board):
    col_choice = -1
    while col_choice < 0 or col_choice > 6:
        try:
            if gui_board is not None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (x_pos,y_pos) = event.pos
                        col_choice = x_pos // size
                        if debug > 0:
                            print(f'Dropping piece in column {col_choice}')
                        
            if gui_board is None:
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
        if gui_board is not None:
            pass
        print("That column is full, pick another column")

    draw_board(board,gui_board,size)