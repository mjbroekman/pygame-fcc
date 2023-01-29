'''
snake.py - A Python implementation of the 'Snake' game using pyGame

Based on:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#snake-python-project

'''
import math
import random
import pygame
import sys
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox

class Segment(object):
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        (self._row,self._col) = start
        self._dirnx = dirnx
        self._dirny = dirny
        self._color = color

    def move(self,dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

    def get_pos(self):
        return (self._row,self._col)

class Snake(object):
    body = [] # List of Segment objects
    turns = {} # List of turns
    def __init__(self, color, pos):
        self.alive = True
        self._color = color
        self._head = Segment(start=pos,color=color)
        self.body.append(self._head)
        self._dirnx = 0
        self._dirny = 1

    @property
    def alive(self) -> bool:
        return self._alive
    
    @alive.setter
    def alive(self,state:bool):
        self._alive = state

    def move(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
            
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                print('Turn left')
                self._dirnx = -1
                self._dirny = 0
                self.turns[self._head.get_pos()] = (self._dirnx,self._dirny)


            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                print('Turn up')
                self._dirnx = 0
                self._dirny = -1
                self.turns[self._head.get_pos()] = (self._dirnx,self._dirny)

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                print('Turn right')
                self._dirnx = 1
                self._dirny = 0
                self.turns[self._head.get_pos()] = (self._dirnx,self._dirny)

            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                print('Turn down')
                self._dirnx = 0
                self._dirny = 1
                self.turns[self._head.get_pos()] = (self._dirnx,self._dirny)

        # for segment in self.body:
        #     if segment.get_pos() == self._head.get_pos():
        #         # We're moving the head
        #         segment.move(self._dirnx,self._dirny)
            
        #     else:
        #         # We're moving a body segment
        #         segment.follow()
                
    def reset(self):
        pass

    def addSegment(self):
        pass

    def draw(self):
        pass

class Board(object):
    def __init__(self,width,height,rows,cols,bgcolor,fgcolor):
        _real_width = ( width // cols ) * cols
        _real_height = ( height // rows ) * rows
        self.width = _real_width
        self.height = _real_height
        self.rows = rows
        self.cols = cols
        self._bgcolor = bgcolor
        self._fgcolor = fgcolor
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

    def drawGrid(self):
        # Draw horizontal line
        for y_val in range(0,self.height+1,self.row_height):
            print(f"Drawing horizontal line from 0,{y_val} to {self.width},{y_val} on {self._window}. color = {self._fgcolor}")
            pygame.draw.line(self._window,self._fgcolor,(0,y_val),(self.width,y_val),2)

        # Draw vertical line
        for x_val in range(0,self.width+1,self.col_width):
            print(f"Drawing vertical line from {x_val},0 to {x_val},{self.height} on {self._window}. color = {self._fgcolor}")
            pygame.draw.line(self._window,self._fgcolor,(x_val,0),(x_val,self.height),2)

    def redrawWindow(self):
        print("Redrawing window...")
        print(f"Filling {self._window} with {self._bgcolor}")
        self._window.fill(self._bgcolor) # Fill the surface with the background color
        self.drawGrid()

class Game():
    def __init__(self,width,height,rows,cols,bgcolor,sncolor,skcolor,fgcolor):
        pygame.display.set_caption('Snake Game')

        self.window = Board(width,height,rows,cols,bgcolor,fgcolor)
        pygame.display.update()
        self.snake = Snake(sncolor,(rows // 2,cols // 2)) # Color is an RGB tuple
        self._snackColor = skcolor
        self.clock = pygame.time.Clock()

    def randomSnack(self,rows,items):
        pass

    def message_box(self,subject,content):
        pass

    def play(self):

        while self.snake.alive:
            pygame.display.update()
            self.window.redrawWindow()
            pygame.time.delay(100) # delay between loop activity aka game 'tick'
            self.clock.tick(10)    # Sets game refresh to 10 frames per second

width = 1000
height = 1000
rows = 2 # Make sure this divides height evenly
cols = 2 # Make sure this divides width evenly
bgcolor = (0,0,0) # Make the background black. This should be an RGB tuple.
sncolor = (255,0,0) # Make the snake red. This should be an RGB tuple.
skcolor = (0,255,0) # Make the snacks green. This should be an RGB tuple
fgcolor = (255,255,255) # Make the foreground white. These are the lines. This should be an RGB tuple

if __name__ == '__main__':
    pygame.init()
    game = Game(width,height,rows,cols,bgcolor,sncolor,skcolor,fgcolor)
    game.play()
