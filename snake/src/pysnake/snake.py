'''
snake.py - A Python implementation of the 'Snake' game using pyGame

Based on:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#snake-python-project

'''
import math
import random
import pygame
import sys
import webcolors

from pygame.locals import *
import tkinter as tk
from tkinter import messagebox

class Segment(object):
    def __init__(self,start,dirnx=1,dirny=0,cell_x=10,cell_y=10,color=(255,0,0)):
        (self._row,self._col) = start
        self._dirnx = dirnx
        self._dirny = dirny
        self._width = cell_x
        self._height = cell_y
        self._color = color
        self._old_pos = (self._row,self._col)

    def move(self,dirnx, dirny):
        self._dirnx = dirnx
        self._dirny = dirny
        self._old_pos = (self._row,self._col)
        self._row += self._dirnx
        self._col += self._dirny

    def follow(self,segment):
        self._old_pos = self.get_pos()
        (self._row,self._col) = segment.get_old_pos()

    def draw(self, surface):
        pygame.draw.rect(surface,self._color,Rect(self._row*self._width,self._col*self._height,self._width,self._height))

    def get_pos(self):
        return (self._row,self._col)
    
    def get_old_pos(self):
        return self._old_pos

class Snake(object):
    body = [] # List of Segment objects

    def __init__(self,bodycolor,headcolor,pos,cell_x,cell_y,debug):
        self.alive = True
        self._color = bodycolor
        self._cellx = cell_x
        self._celly = cell_y
        self._head = Segment(start=pos,cell_x=cell_x,cell_y=cell_y,color=headcolor)
        self.body.append(self._head)
        self._dirnx = 0
        self._dirny = 1
        self.debug = debug

    @property
    def alive(self) -> bool:
        return self._alive
    
    @property
    def size(self) -> int:
        return len(self.body)

    @alive.setter
    def alive(self,state:bool):
        self._alive = state

    def move(self,cols,rows):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                return False
            
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if self.debug > 1:
                    print('Turn left')
                self._dirnx = -1
                self._dirny = 0


            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                if self.debug > 1:
                    print('Turn up')
                self._dirnx = 0
                self._dirny = -1

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if self.debug > 1:
                    print('Turn right')
                self._dirnx = 1
                self._dirny = 0

            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if self.debug > 1:
                    print('Turn down')
                self._dirnx = 0
                self._dirny = 1
                
        for segment in self.body:
            if segment.get_pos() == self._head.get_pos():
                # We're moving the head
                (cur_col,cur_row) = segment.get_pos()
                if self.debug > 1:
                    print(f"We are at {cur_row} {cur_col} moving {self._dirnx} {self._dirny} on a board that is {rows} rows and {cols} cols")

                if cur_row == 0 and self._dirny == -1: # Top row, moving up
                    self._dirny = 0
                    self._dirnx = 1

                    if cur_col == (cols - 1):
                        self._dirnx = -1

                if cur_row == (rows - 1) and self._dirny == 1: # Bottom row, moving down
                    self._dirny = 0
                    self._dirnx = -1

                    if cur_col == 0:
                        self._dirnx = 1

                if cur_col == 0 and self._dirnx == -1: # Left column, moving left
                    self._dirnx = 0
                    self._dirny = -1

                    if cur_row == 0:
                        self._dirny = 1

                if cur_col == (cols - 1) and self._dirnx == 1: # Right column, moving right
                    self._dirnx = 0
                    self._dirny = 1

                    if cur_row == (rows - 1):
                        self._dirny = -1

                segment.move(self._dirnx,self._dirny)

                for tail_segment in self.body[1:]:
                    if tail_segment.get_pos() == self._head.get_pos():
                        # We bit ourselves... we die. return False for the move.
                        return False

            else:
                # We're moving a body segment
                segment.follow(previous_segment)

            # Set the previous_segment to the current segment before we move on to the next segment in the body            
            previous_segment = segment
        
        # If we made it through all the looping, we are still alive... return True for the move.
        return True

    def draw(self,surface):
        for segment in self.body:
            segment.draw(surface)

    def get_head_pos(self):
        return self._head.get_pos()

    def get_snake_pos(self):
        _all_pos = []
        for segment in self.body:
            _all_pos.append(segment.get_pos())
        
        return _all_pos

    def addSegment(self):
        p_segment = self.body[-1]
        self.body.append(Segment(start=p_segment.get_old_pos(),cell_x=self._cellx,cell_y=self._celly,color=self._color))

class Board(object):
    def __init__(self,width,height,rows,cols,bgcolor,fgcolor,debug):
        _real_width = ( width // cols ) * cols
        _real_height = ( height // rows ) * rows
        self.width = _real_width
        self.height = _real_height
        self.rows = rows
        self.cols = cols
        self._bgcolor = bgcolor
        self._fgcolor = fgcolor
        self.debug = debug
        self._window = pygame.display.set_mode((self.width+1,self.height+1))
        pygame.display.update()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,size):
        self._width = size
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,size):
        self._height = size
    
    @property
    def rows(self):
        return self._rows
    
    @property
    def row_height(self):
        return self._row_height

    @rows.setter
    def rows(self,count):
        self._rows = count
        self._row_height = self.height // count
    
    @property
    def cols(self):
        return self._cols

    @property
    def col_width(self):
        return self._col_width

    @cols.setter
    def cols(self,count):
        self._cols = count
        self._col_width = self.width // count

    def get_surface(self):
        return self._window

    def drawGrid(self):
        # Draw horizontal line
        for y_val in range(0,self.height+1,self.row_height):
            if self.debug > 2:
                print(f"Drawing horizontal line from 0,{y_val} to {self.width},{y_val} on {self._window}. color = {self._fgcolor}")
            pygame.draw.line(self._window,self._fgcolor,(0,y_val),(self.width,y_val),2)

        # Draw vertical line
        for x_val in range(0,self.width+1,self.col_width):
            if self.debug > 2:
                print(f"Drawing vertical line from {x_val},0 to {x_val},{self.height} on {self._window}. color = {self._fgcolor}")
            pygame.draw.line(self._window,self._fgcolor,(x_val,0),(x_val,self.height),2)

    def redrawWindow(self,snacklist):
        if self.debug > 1:
            print("Redrawing window...")
            print(f"Filling {self._window} with {self._bgcolor}")
        self._window.fill(self._bgcolor) # Fill the surface with the background color
        self.drawGrid()
        for snack in snacklist:
            snack.draw(self._window,self.col_width,self.row_height)


class Snack(object):
    _poisonous = (200,250,15)

    def __init__(self,pos,skcolor,poison=False):
        (self._col,self._row) = pos
        self._poison = poison
        self.color = self._poisonous if self.poison else skcolor
        self._age = 0

    @property
    def position(self):
        return (self._col,self._row)

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,incr):
        self._age += incr
        self.color = tuple(int(a + (b - a) * (self._age/25)) for a, b in zip(self.color, self._poisonous))
        if self.color == self._poisonous:
            self._poison = True

    @property
    def poison(self):
        return self._poison

    def draw(self,surface,width,height):
        pygame.draw.rect(surface,self.color,Rect(self._col*width,self._row*height,width,height))


class Game():
    _snacks = []

    def __init__(self,width,height,rows,cols,bgcolor,sncolor,hdcolor,skcolor,fgcolor,max_snacks,debug):
        pygame.init()
        pygame.display.set_caption('Snake Game')
        self.window = Board(width,height,rows,cols,bgcolor,fgcolor,debug)
        pygame.display.update()
        self.snake = Snake(sncolor,hdcolor,(rows // 2,cols // 2),width // cols,height // rows,debug) # Color is an RGB tuple
        self.clock = pygame.time.Clock()
        self.debug = debug
        self.snack_color = skcolor
        self.bgcolor = bgcolor
        self.delay = 100
        self.max_snacks = max_snacks

    def randomSnack(self,snake):
        #                              X                                  Y
        new_snack = (random.randrange(0,self.window.cols),random.randrange(0,self.window.cols))
        if len(self._snacks) < self.max_snacks:
            if new_snack not in snake.get_snake_pos() and new_snack not in self._snacks:
                if self.debug > 0:
                    print("Attempting to add a snack... at {}".format(new_snack))

                poison = False
                if random.randint(0,(rows*cols)) < self.snake.size:
                    poison = True

                self._snacks.append(Snack((new_snack),self.snack_color,poison))

            new_snack = (random.randrange(0,self.window.cols),random.randrange(0,self.window.cols))

    def message_box(self,subject,content):
        pygame.display.set_caption("Game Over")
        surface = self.window.get_surface()
        font = pygame.font.Font('freesansbold.ttf', 24)
        top_msg = font.render(subject,True,"white","black")
        mid_msg = font.render(content,True,"white","black")
        end_msg = font.render("Press ESC to quit",True,"white","black")
        msgBox1 = top_msg.get_rect()
        msgBox2 = mid_msg.get_rect()
        msgBox3 = end_msg.get_rect()
        msgBox1.center = (self.window.width // 2, self.window.height // 4)
        msgBox2.center = (self.window.width // 2, self.window.height // 2)
        msgBox3.center = (self.window.width // 2, (self.window.height // 4) * 3)
        print(subject)
        print(content)

        while True:
            surface.fill(self.bgcolor)
            surface.blit(top_msg,msgBox1)
            surface.blit(mid_msg,msgBox2)
            surface.blit(end_msg,msgBox3)
            pygame.display.update()

            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

    def play(self):
        _moves = 0
        _score = 0
        while self.snake.alive:
            _moves += 1
            self.snake.alive = self.snake.move(self.window.rows,self.window.cols)
            self.snake.draw(self.window.get_surface())

            # 10% change to generate a snack...
            if random.randint(1,100) < 10:
                self.randomSnack(self.snake)

            for snack in self._snacks:
                if self.debug > 0:
                    print("Snack at {}  || Snake Head at {}".format(snack,self.snake.get_head_pos()))
                if snack.position == self.snake.get_head_pos():
                    if snack.poison:
                        self.snake.alive = False
                        self.endgame("You ate a poison snack and died!",score=_score)

                    self.snake.addSegment()
                    self._snacks.remove(snack)
                    _score += snack.age // 2

                elif _moves % 75 and random.randint(0,100) > 50:
                    snack.age = 1

                if random.randint(self.window.rows,(self.window.rows*self.window.cols)) < snack.age:
                    self._snacks.remove(snack)

            # Reduce game delay (speed up the game) 
            if random.randint(0,100) > (100 - self.snake.size) and self.delay > 10:
                if self.debug > 3:
                    print("Faster! Hahahahahahaha!")
                self.delay -= 1

            pygame.display.update()

            self.window.redrawWindow(self._snacks)
            pygame.time.delay(self.delay) # delay between loop activity aka game 'tick'
            self.clock.tick(1000)    # Sets game refresh to 10 frames per second

        _snake_head = self.snake.get_head_pos()
        if _snake_head in self.snake.get_snake_pos()[1:]:
            self.endgame("You are an ouroboros.",score=_score)
        
        self.endgame("Exiting the game",score=_score)

    def endgame(self,msg="",score=-1):
        bonus = 100 - self.delay  # Give bonus points for the faster you were moving
        final_score = score + bonus
        end_msg = f"Final Score: {final_score} (Life: {score}, Bonus: {bonus})"
        self.message_box(msg,end_msg)



# Set some defaults...
width = 1000
height = 1000
rows = 100 # Make sure this divides height evenly
cols = 100 # Make sure this divides width evenly
bgcolor = (0,0,0) # Make the background black. This should be an RGB tuple.
sncolor = (255,0,0) # Make the snake red. This should be an RGB tuple.
hdcolor = (255,0,0) # Make the head of the snake red. This should be an RGB tuple.
skcolor = (0,255,0) # Make the snacks green. This should be an RGB tuple
fgcolor = (255,255,255) # Make the foreground white. These are the lines. This should be an RGB tuple
max_snack = 1

if __name__ == '__main__':
    # Use argparse to read command-line arguments to create the board...
    import argparse
    parser = argparse.ArgumentParser(description="A game of Snake implemented in Python.")
    parser.add_argument("--width",action="store",type=int,help="Board width",default=100)
    parser.add_argument("--height",action="store",type=int,help="Board height",default=100)
    parser.add_argument("--rows",action="store",type=int,help="Number of rows", default=10)
    parser.add_argument("--cols",action="store",type=int,help="Nuimber of columns", default=10)
    parser.add_argument("--bgcolor",action="store",type=str,help="Background color",default="black")
    parser.add_argument("--snack",action="store",type=str,help="Snack color",default="lime")
    parser.add_argument("--snake",action="store",type=str,help="Snake color",default="olive")
    parser.add_argument("--head",action="store",type=str,help="Color of snake head",default="red")
    parser.add_argument("--fgcolor",action="store",type=str,help="Foreground color",default="white")
    parser.add_argument("--debug","-d",action="count",help="Set debug level. Can be used multiple times to increase debug level",default=0)
    parser.add_argument("--maxsnack",action="store",type=int,help="Maximum number of simultaneous snacks",default=1)
    args = parser.parse_args()

    try:
        _bgcolor = webcolors.name_to_rgb(args.bgcolor)
    except ValueError:
        if args.debug > 0:
            print(f"Unknown color: '{args.bgcolor}'. Defaulting to 'black'")
        _bgcolor = bgcolor

    try:
        _snake = webcolors.name_to_rgb(args.snake)
    except ValueError:
        if args.debug > 0:
            print(f"Unknown color: '{args.snake}'. Defaulting to 'red'")
        _snake = sncolor

    try:
        _head = webcolors.name_to_rgb(args.head)
    except ValueError:
        if args.debug > 0:
            print(f"Unknown color: '{args.head}'. Defaulting to 'red'")
        _head = hdcolor
    
    try:
        _snack = webcolors.name_to_rgb(args.snack)
    except ValueError:
        if args.debug > 0:
            print(f"Unknown color: '{args.snack}'. Defaulting to 'green'")
        _snack = skcolor
    
    try:
        _fgcolor = webcolors.name_to_rgb(args.fgcolor)
    except ValueError:
        if args.debug > 0:
            print(f"Unknown color: '{args.fgcolor}'. Defaulting to 'white'")
        _fgcolor = fgcolor

    max_snack = args.maxsnack    
    width = args.width
    height = args.height
    rows = args.rows
    cols = args.cols

    game = Game(width,height,rows,cols,_bgcolor,_snake,_head,_snack,_fgcolor,max_snack,args.debug)
    game.play()
