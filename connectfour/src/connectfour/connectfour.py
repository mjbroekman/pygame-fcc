'''
connectfour.py

By: Maarten Broekman

Based on: https://www.freecodecamp.org/news/python-projects-for-beginners/#connect-four-python-project

Skills:
- Simple numpy matrices
- Pointer following in PyGame
- Text in PyGame

Add-ons:
- Numpy sequence searching
- Numpy diagonals
- Dynamic font size and position changes based on board size
- Handling ties

'''
import numpy as np
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

    if repr(board).count("0") == 0:
        return (True,"It's a tie!")

    # For row or column wins, this is easy.
    # Simply iterate over the rows, rotate the matrix, iterate again
    for layout in board, np.rot90(board):
        row_count = len(layout)
        for row in range(0,row_count):
            row_arr = list(layout[row])
            for i in range(0,(len(row_arr) - 3)):
                if row_arr[i:i+4] == _p1_seq:
                    return (True,"Player 1 WINS!")

                if row_arr[i:i+4] == _p2_seq:
                    return (True, "Player 2 WINS!")
        
        # At the same time, we can take the length of the row div2
        # Then check all the diagonals from -div to +div!!!
        for diagonal in range(-row_count // 2,row_count // 2):
            diag = np.diag(layout,diagonal)
            row_arr = list(diag)
            if len(row_arr) >= 4:
                for i in range(0,(len(row_arr) - 3)):
                    if row_arr[i:i+4] == _p1_seq:
                        return (True, "Player 1 WINS ON A DIAGONAL!")

                    if row_arr[i:i+4] == _p2_seq:
                        return (True, "Player 2 WINS ON A DIAGONAL!")

    return (False,"")


def draw_board(board,gui_board,size):
    print(board)
    print('='*20)
    print('='*20)
    if gui_board is not None:
        for column in range(gui_board.get_width() // size):
            for row in range(gui_board.get_height() // size):
                if row == 0:
                    pygame.draw.rect(gui_board,(0,0,0),(column*size,row*size,size,size))
                else:
                    pygame.draw.rect(gui_board,(0,0,255),(column*size,row*size,size,size))
                    center_x = (column * size) + (size // 2)
                    center_y = (row * size) + (size // 2)
                    color = (0,0,0)
                    if board[row-1][column] == 1:
                        color = (255,0,0)
                    if board[row-1][column] == 2:
                        color = (255,255,0)
                    pygame.draw.circle(gui_board,color,(center_x,center_y), float(size // 2))
        
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
game_over = False
end_msg = "Game is not over! Keep playing!"

while not game_over:
    draw_board(board,gui_board,size)
    col_choice = -1
    while col_choice < 0 or col_choice > 6:
        try:
            if gui_board is not None:
                color = (0,0,0)
                if player_turn == 1:
                    color = (255,0,0)
                if player_turn == 2:
                    color = (255,255,0)
                (x_pos,y_pos) = pygame.mouse.get_pos()
                column = x_pos // size
                center_x = (column * size) + (size // 2)
                center_y = size // 2
                pygame.draw.rect(gui_board,(0,0,0),(0,0,cols*size,size))
                pygame.draw.circle(gui_board,color,(center_x,center_y),float(size // 2))
                pygame.display.update()

                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                        game_over = True

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

        (game_over, end_msg) = is_game_over(board)

    else:
        print("That column is full, pick another column")


draw_board(board,gui_board,size)
print(end_msg)
if end_msg.find("Player 1") > -1:
    text_color = "red"
elif end_msg.find("Player 2") > -1:
    text_color = "yellow"
else:
    text_color = "white"

pygame.display.set_caption("Game Over")
font = pygame.font.Font('freesansbold.ttf', 6 * cols)
top_msg = font.render(end_msg,True,text_color,"black")
end_msg = font.render("Press a key to quit",True,"white","black")
msgBox1 = top_msg.get_rect()
msgBox3 = end_msg.get_rect()
msgBox1.center = (gui_board.get_width() // 2, gui_board.get_height() // 4)
msgBox3.center = (gui_board.get_width() // 2, (gui_board.get_height() // 4) * 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            pygame.quit()
            sys.exit()

    gui_board.blit(top_msg,msgBox1)
    gui_board.blit(end_msg,msgBox3)
    pygame.display.update()
