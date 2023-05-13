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
                'oo',
                'oo'
            ]
        ]
    },
    'S': {
        'name': 'S',
        'color': webcolors.name_to_hex('green'),
        'turns':[
            [
                '.oo',
                'oo.'
            ],
            [
                '.o.',
                '.oo',
                '..o'
            ]
        ]
    },
    'Z': {
        'name': 'Z',
        'color': webcolors.name_to_hex('red'),
        'turns':[
            [
                'oo.',
                '.oo',
            ],
            [
                '.o',
                'oo',
                'o.'
            ]
        ]
    },
    'I': {
        'name': 'I',
        'color': webcolors.name_to_hex('cyan'),
        'turns':[
            [
                '..o',
                '..o',
                '..o',
                '..o'
            ],
            [
                '....',
                'oooo'
            ]
        ]
    },
    'J': {
        'name': 'J',
        'color': webcolors.name_to_hex('orange'),
        'turns':[
            [
                'o..',
                'ooo'
            ],
            [
                '.oo',
                '.o.',
                '.o.'
            ],
            [
                '...',
                'ooo',
                '..o'
            ],
            [
                '.o',
                '.o',
                'oo'
            ],
        ]
    },
    'L': {
        'name': 'L',
        'color': webcolors.name_to_hex('blue'),
        'turns':[
            [
                '..o',
                'ooo'
            ],
            [
                '.o.',
                '.o.',
                '.oo'
            ],
            [
                '...',
                'ooo',
                'o..'
            ],
            [
                'oo',
                '.o',
                '.o'
            ],
        ]
    },
    'T': {
        'name': 'T',
        'color': webcolors.name_to_hex('magenta'),
        'turns':[
            [
                '.o.',
                'ooo'
            ],
            [
                '.o.',
                '.oo',
                '.o.'
            ],
            [
                '...',
                'ooo',
                '.o.'
            ],
            [
                '.o',
                'oo',
                '.o'
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
    def __init__(self, x, y, shapedef):
        self._x = x
        self._y = y
        self.shape = shapedef['name']
        self.color = shapedef['color']
        self.turns = shapedef['turns']
        self.turn_length = len(self.turns)
        self.rotation = random.randrange(self.turn_length)
        self.last = { "none": 0 }

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,val):
        self._x = val

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self,val):
        self._y = val

    def rotate(self):
        self.last = { "rotation": self.rotation }
        self.rotation = (self.rotation + 1) % self.turn_length
    
    def drop(self):
        self.last = { "y": self.y }
        self.y -= 1
    
    def left(self):
        self.last = { "x": self.x }
        self.x -= 1
    
    def right(self):
        self.last = { "x": self.x }
        self.x += 1
    
    def get_form(self) -> list:
        return self.turns[self.rotation]

    def undo_last(self):
        if list(self.last.keys())[0] == "rotation":
            self.rotation = list(self.last.values())[0]
        if list(self.last.keys())[0] == "x":
            self.x = list(self.last.values())[0]
        if list(self.last.keys())[0] == "y":
            self.y = list(self.last.values())[0]


def create_grid(x_size, y_size, locked_pos = {}) -> list:
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

def convert_shape_format(shape: Piece) -> list:
    '''
    Differs from https://www.youtube.com/watch?v=XGf2GcyHPhc&t=11679s because I
    trimmed the shapes to their minimum sizes. There shouldn't be a need to
    adjust like in the video.
    '''
    positions = []
    form = shape.get_form()

    for i, line in enumerate(form):
        row = list(line)
        for j, col in enumerate(row):
            if col == 'o':
                positions.append((shape.x + j, shape.y + i - 4))

    return positions

def valid_space(piece: Piece, grid) -> bool:
    accepted_pos = [(j,i) for j in range(len(grid[i])) for i in range(len(grid))]

    for pos in convert_shape_format(piece):
        if pos not in accepted_pos and pos[1] > -1:
            return False
    
    return True

def check_lost():
    pass

def get_shape():
    # Return a random key into the shapes dict
    return Piece(block_x_cnt // 2, 0, shapes[random.choice(shape_list)])

def draw_text_middle():
    pass

def draw_grid(surface: pygame.Surface, grid):
    for y in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (top_left_x, (top_left_y + y * block_size)), (top_left_x + play_width, (top_left_y + y * block_size)) )
    for x in range(len(grid[y])):
        pygame.draw.line(surface, (128,128,128), (top_left_x + (x * block_size), top_left_y), (top_left_x + (x * block_size), top_left_y + play_height) )

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

    # Draw the play field on top of the red background
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, color=grid[y][x], rect=(top_left_x + (x * block_size), top_left_y + (y * block_size), block_size, block_size), width=1)

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
                    current_piece.left()
                    if not(valid_space(current_piece,grid)):
                        current_piece.undo_last()
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    current_piece.right()
                    if not(valid_space(current_piece,grid)):
                        current_piece.undo_last()
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    current_piece.rotate()
                    if not(valid_space(current_piece,grid)):
                        current_piece.undo_last()

                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    current_piece.drop()
                    if not(valid_space(current_piece,grid)):
                        current_piece.undo_last()

        # grid = create_grid(locked_pos)


def main_menu(block_x_cnt, block_y_cnt):
    main(block_x_cnt, block_y_cnt)
    pass


main_menu(block_x_cnt, block_y_cnt)
