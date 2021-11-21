"""
name: Ryan and John
file: search_maze_after.py
data: Nov 17, 2021
course: CS321
description: Refactoring Project Extension
"""


from tkinter.constants import X
import turtle
import time
from multiprocessing import Process

class MazeGame: 

    def __init__(self):
        self.window = self.make_window("MazeGame", "slate gray")
        self.turt = self.make_turtle("square")

        self.x_offset = -150
        self.y_offset = 200
        self.tile_size = 50

        self.steps = 0
        
        self.grid = []
        
        self.filename = "maze4.txt"

    def make_window(self, window_title, bgcolor):
        window = turtle.getscreen()
        window.title(window_title)
        window.bgcolor(bgcolor)
        return window
        
    def make_turtle(self, shape):
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.shape(shape)
        turt.shapesize(2.5,2.5)
        return turt
        
    def teleport(self, x_pos, y_pos):
        self.turt.up()
        self.turt.goto(x_pos, y_pos)
        self.turt.down()
        
    
    def draw_grid(self):

        self.window.tracer(False)
        
        self.teleport(self.x_offset, self.y_offset)

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                
                self.teleport(self.x_offset + col * self.tile_size, self.y_offset -row * self.tile_size)

                if self.grid[row][col] == 'X':
                    self.turt.color('grey', "black")
                    self.turt.stamp()
                
                elif self.grid[row][col] == 'S':
                    self.turt.color('grey', "yellow")
                    self.turt.stamp()
                
                elif self.grid[row][col] == 'E':
                    self.turt.color('grey', "red")
                    self.turt.stamp()

                elif self.grid[row][col] == 'P':
                    self.turt.color('grey', "royalblue")
                    self.turt.stamp()

                elif self.grid[row][col] == 'T':
                    self.turt.color('grey', "light blue")
                    self.turt.stamp()

                elif self.grid[row][col] == 'D':
                    self.turt.color('gainsboro', "gray")
                    self.turt.stamp()
                
                else:
                    self.turt.color( 'grey', "white")
                    self.turt.stamp()
        
        self.window.tracer(True)


    def find_start(self):

        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                if self.grid[row][col] == 'S':
                    return (row, col)



    def read_grid(self):

        file = open(self.filename)
        line = file.readline()
        line = line.replace('\n', '')

        while line:
            tokens = line.split(',')
            self.grid.append(tokens)
            line = file.readline()
            line = line.replace('\n', '')

        return self.grid


    def search_from(self, row, col):

        self.steps += 1

        if row < 0 or col < 0 or row == len(self.grid) or col == len(self.grid[0]):
            return False

        if self.grid[row][col] == 'X' or self.grid[row][col] == 'T' or self.grid[row][col] == 'D':
            return False

        if self.grid[row][col] == 'E':
            return True
        
        if self.grid[row][col] != 'S':
            self.grid[row][col] = 'T'

        self.draw_grid()

        time.sleep(0.25)

        found = (self.search_from(row-1, col)
                or self.search_from(row+1, col)
                or self.search_from(row, col-1)
                or self.search_from(row, col+1)
                )

        if found and self.grid[row][col] != 'S':
            self.grid[row][col] = 'P'
            return True
        elif self.grid[row][col] != 'S':
            self.grid[row][col] = 'D'
        

    def main(self):

        playground = self.read_grid()

        row, col = self.find_start()
        self.search_from(row, col)

        path = []
        for row in range(len(playground)):
            for col in range(len(playground[0])):
                if playground[row][col] == 'P':
                    path.append((row, col))

        print('path length:', len(path))

        self.draw_grid()
        
        time.sleep(4)

        print("number of steps taken to reach answer:", self.steps)
        


if __name__ == "__main__":
    the_game = MazeGame()
    the_game.main()


