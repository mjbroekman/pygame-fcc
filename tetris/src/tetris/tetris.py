'''
tetris.py - A Python Implementation of Tetris using PyGame

based on FreeCodeCamp's Tetris Python Project:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#tetris-python-project

'''
import pygame
import webcolors

shapes = {
    'O': {
        'color': webcolors.name_to_hex('yellow'),
        'turns': [
            [
                '.....',
                '.....',
                '.oo..',
                '.oo..',
                '.....'
            ]
        ]
    },
    'S': {
        'color': webcolors.name_to_hex('green'),
        'turns':[
            [
                '.....',
                '.....',
                '..oo.',
                '.oo..',
                '.....'
            ],
            [
                '.....',
                '..o..',
                '..oo.',
                '...o.',
                '.....'
            ]
        ]
    },
    'Z': {
        'color': webcolors.name_to_hex('red'),
        'turns':[
            [
                '.....',
                '.....',
                '.oo..',
                '..oo.',
                '.....'
            ],
            [
                '.....',
                '...o.',
                '..oo.',
                '..o..',
                '.....'
            ]
        ]
    },
    'I': {
        'color': webcolors.name_to_hex('cyan'),
        'turns':[
            [
                '..o..',
                '..o..',
                '..o..',
                '..o..',
                '.....'
            ],
            [
                '.....',
                'oooo.',
                '.....',
                '.....',
                '.....'
            ]
        ]
    },
    'J': {
        'color': webcolors.name_to_hex('orange'),
        'turns':[
            [
                '.....',
                '.o...',
                '.ooo.',
                '.....',
                '.....'
            ],
            [
                '.....',
                '..oo.',
                '..o..',
                '..o..',
                '.....'
            ],
            [
                '.....',
                '.....',
                '.ooo.',
                '...o.',
                '.....'
            ],
            [
                '.....',
                '..o..',
                '..o..',
                '.oo..',
                '.....'
            ],
        ]
    },
    'L': {
        'color': webcolors.name_to_hex('blue'),
        'turns':[
            [
                '.....',
                '...o.',
                '.ooo.',
                '.....',
                '.....'
            ],
            [
                '.....',
                '..o..',
                '..o..',
                '..oo.',
                '.....'
            ],
            [
                '.....',
                '.....',
                '.ooo.',
                '.o...',
                '.....'
            ],
            [
                '.....',
                '.oo..',
                '..o..',
                '..o..',
                '.....'
            ],
        ]
    },
    'T': {
        'color': webcolors.name_to_hex('magenta'),
        'turns':[
            [
                '.....',
                '..o..',
                '.ooo.',
                '.....',
                '.....'
            ],
            [
                '.....',
                '..o..',
                '..oo.',
                '..o..',
                '.....'
            ],
            [
                '.....',
                '.....',
                '.ooo.',
                '..o..',
                '.....'
            ],
            [
                '.....',
                '..o..',
                '.oo..',
                '..o..',
                '.....'
            ],
        ]
    },
}

border_width = 500
border_height = 100
block_size = 30      # width and height of blocks
block_x_cnt = 10     # 10 blocks wide * 30 cells => 300 pixel wide board
block_y_cnf = 20     # 20 blocks high * 30 cells => 600 pixel high board
play_width = block_x_cnt * block_size
play_height = block_y_cnf * block_size
#
# screen width = play_width * block_size + border_width
# screen height = play_height * block_size + border_height
#
# screen = 
#   |------------------------------------------------------------------|
#   |                         border_height                            |
#   |-------------------X--------------------------|-------------------|
#   |                   |      ^                   |                   |
#   | border_width // 2 | <--- | play_width ---->  | border_width // 2 |
#   |                   |      | play_height       |                   |
#   |                   |      v                   |                   |
#   |------------------------------------------------------------------|
#
# top left corner (X,Y) = border_width // 2, border_height
top_left_x = border_width // 2
top_left_y = border_height

class Piece(object):
    pass

def create_grid(locked_pos = []):
    pass

def convert_shape_format():
    pass

def valid_space():
    pass

def check_lost():
    pass

def get_shape():
    pass

def draw_text_middle():
    pass

def draw_grid():
    pass

def clear_rows():
    pass

def draw_next_shape():
    pass

def draw_window():
    pass

def main():
    pass

def main_menu():
    pass


main_menu()
