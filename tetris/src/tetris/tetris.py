'''
tetris.py - A Python Implementation of Tetris using PyGame

based on FreeCodeCamp's Tetris Python Project:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#tetris-python-project

'''
import pygame
import webcolors
import random

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
    def __init__(self, x, y, shape, shapedef):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shapedef['color']
        self.turns = shapedef['turns']
        self.rotation = random.choice(self.turns)


def create_grid(x_size, y_size,locked_pos = {}):
    # initialize the grid to an x_size wide, y_size high 2D list with each item being "black"
    # we don't care about the variable for the loops, so we can use _ ... if we're being
    # explicit, the inner list is x and the outer list is y
    grid = [[(0,0,0) for _ in range(x_size)] for _ in range(y_size)]

    # Loop over the grid now to see if any positions are in locked_pos{}
    # If they are, set the color to what is in locked_pos{}
    # the video used i instead of y and j instead of x. I changed that for clarity.
    ##
    # Commented out because this exhaustive loop over grid is inefficient
    ##
    # for y in range(len(grid)):
    #     for x in range(len(grid[y])):
    #         if (x,y) in locked_pos:
    #             c = locked_pos[(x,y)]
    #             grid[x][y] = c
    ##
    # There will ALWAYS be fewer items in locked_pos than in grid...
    # Loop over locked_pos instead
    for (x,y), color in locked_pos.items():
        grid[x][y] = color

    return grid

def convert_shape_format():
    pass

def valid_space():
    pass

def check_lost():
    pass

def get_shape():
    # Return a random key into the shapes dict
    return random.choice(shapes.keys())


def draw_text_middle():
    pass

def draw_grid(surface: pygame.Surface, grid):
    # fill the surface with black
    surface.fill(0,0,0)

    # initialize a font for our text
    pygame.font.init()
    # Set to Arial... for whatever
    font = pygame.font.SysFont('Arial',60)
    # Create a label using the font, anti-alias it, and make it white
    label = font.render('Tetris',1,(255,255,255))
    # blit it to the surface in the top center
    surface.blit(label,(top_left_x + play_width // 2 - label.get_width // 2), border_height // 2)

    # Draw the red play background
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)

    # Draw the play field on top of the red background
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, grid[x][y], (top_left_x + (x * block_size), top_left_y + (y * block_size), block_size, block_size), 0)

    # Update the display
    pygame.display.update()


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
