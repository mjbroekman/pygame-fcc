'''
tetris.py - A Python Implementation of Tetris using PyGame

based on FreeCodeCamp's Tetris Python Project:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#tetris-python-project

'''
import pygame
import webcolors
import random
import pprint

shapes = {
    'O': {
        'name': 'O',
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
        'name': 'S',
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
        'name': 'Z',
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
        'name': 'I',
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
        'name': 'J',
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
        'name': 'L',
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
        'name': 'T',
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

shape_list = list(shapes.keys())

border_width = 400
border_height = 100
block_size = 30      # width and height of blocks
block_x_cnt = 10     # 10 blocks wide * 30 cells => 300 pixel wide board
block_y_cnt = 20     # 20 blocks high * 30 cells => 600 pixel high board
play_width = block_x_cnt * block_size
play_height = block_y_cnt * block_size
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


def create_grid(x_size, y_size, locked_pos = {}):
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

    pp = pprint.PrettyPrinter(indent=2,compact=True,width=130)
    pp.pprint(grid)
    return grid

def convert_shape_format():
    pass

def valid_space():
    pass

def check_lost():
    pass

def get_shape():
    # Return a random key into the shapes dict
    return shapes[random.choice(shape_list)]


def draw_text_middle():
    pass

def draw_grid(surface: pygame.Surface, grid):
    # Draw the play field on top of the red background
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, color=grid[y][x], rect=(top_left_x + (x * block_size), top_left_y + (y * block_size), block_size, block_size), width=1)


def clear_rows():
    pass

def draw_next_shape():
    pass

def draw_window(surface: pygame.Surface, grid):
    # fill the surface with black
    surface.fill((0,0,0))

    # initialize a font for our text
    pygame.font.init()
    # Set to Arial... for whatever
    font = pygame.font.SysFont('Arial',30)
    # Create a label using the font, anti-alias it, and make it white
    label = font.render('Tetris',1,(255,255,255))
    # blit it to the surface in the top center
    surface.blit(label,((top_left_x + play_width // 2 - label.get_width() // 2), border_height // 2 - label.get_height() // 2))

    # Draw the red play background
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)

    draw_grid(surface,grid)

    # Update the display
    pygame.display.update()


def main(x_size, y_size):
    pygame.init()
    pygame.display.set_caption('pyTris')
    locked_pos = {}
    grid = create_grid(x_size, y_size, locked_pos)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    surface = pygame.display.set_mode((play_width + border_width,play_height + border_height))
    pygame.display.update()

    while run:
        draw_window(surface,grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    run = False
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    '''Move one cell to the left'''
                    pass
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    '''Move one cell to the right'''
                    pass
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    '''Rotate the shape'''
                    pass
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    '''Move cell down'''
                    pass

        # grid = create_grid(locked_pos)


def main_menu(block_x_cnt, block_y_cnt):
    main(block_x_cnt, block_y_cnt)
    pass


main_menu(block_x_cnt, block_y_cnt)
