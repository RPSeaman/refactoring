"""
name: Ryan and John
file: connect-4_after.py
data: Nov 17, 2021
course: CS321
description: Refactoring Project
"""


from tkinter.constants import X
import turtle
import time
from multiprocessing import Process


class MazeGame:
    def __init__(self):
        self.window = self.make_window("MazeGame", "slate gray")
        self.turt = self.make_turtle("square")

        # set offsets and tile size for drawing the grid
        self.x_offset = -150
        self.y_offset = 200
        self.tile_size = 50

        # create an int variable for counting steps
        self.steps = 0

        self.grid = []

        self.filename = "maze1.txt"

    def make_window(self, window_title, bgcolor):
        window = turtle.getscreen()
        window.title(window_title)
        window.bgcolor(bgcolor)
        return window

    def make_turtle(self, shape):
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.shape(shape)
        turt.shapesize(2.5, 2.5)
        return turt

    def teleport(self, x_pos, y_pos):
        self.turt.up()
        self.turt.goto(x_pos, y_pos)
        self.turt.down()

    def draw_grid(self):
        """draws a grid at x_pos, y_pos with a specific tile_size"""

        # turn off tracer for fast drawing
        self.window.tracer(False)

        # move turtle to initial drawing position
        self.teleport(self.x_offset, self.y_offset)

        # go over every cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):

                # move turtle to the position of the cell in the grid
                self.teleport(
                    self.x_offset + col * self.tile_size,
                    self.y_offset - row * self.tile_size,
                )

                # if the cell is an obstacle (X) draw a black dot
                if self.grid[row][col] == "X":
                    # turt.dot(tile_size-5, "Black")
                    self.turt.color("grey", "black")
                    self.turt.stamp()

                # if the cell is the start drawing position (S) draw a yellow dot
                elif self.grid[row][col] == "S":
                    # turt.dot(tile_size-5, "yellow")
                    self.turt.color("grey", "yellow")
                    self.turt.stamp()

                # if the cell is the End position (E) draw a Red dot
                elif self.grid[row][col] == "E":
                    # turt.dot(tile_size-5, "red")
                    self.turt.color("grey", "red")
                    self.turt.stamp()

                # if the cell is part of a path (P) draw a royalblue dot
                elif self.grid[row][col] == "P":
                    # turt.dot(tile_size-5, "royalblue")
                    self.turt.color("grey", "royalblue")
                    self.turt.stamp()

                # if the cell has been tried before (T) draw a light blue dot
                elif self.grid[row][col] == "T":
                    # turt.dot(tile_size-5, "light blue")
                    self.turt.color("grey", "light blue")
                    self.turt.stamp()

                # if the cell is part of a deadend (D) draw a gray dot
                elif self.grid[row][col] == "D":
                    # turt.dot(tile_size-5, "gray")
                    self.turt.color("gainsboro", "gray")
                    self.turt.stamp()

                # else draw a white dot
                else:
                    # turt.dot(tile_size-5, "white")
                    self.turt.color("grey", "white")
                    self.turt.stamp()

        # turn tracer back on
        self.window.tracer(True)

    def find_start(self):
        """finds the start position (S) in the grid
        returns a tuple of start row and col
        """

        # go over every cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                # cell at row, col is 'S' return row and col as a tuple
                if self.grid[row][col] == "S":
                    return (row, col)

    def read_grid(self):
        """reads a maze file and initializes a gird with its contents"""

        # create an empty grid (an empty list called grid)

        # open the text file
        file = open(self.filename)

        # read a line from the file
        line = file.readline()

        # replace \n with nothing
        line = line.replace("\n", "")

        while line:
            # split the line into tokens
            tokens = line.split(",")

            # add the tokens to the grid as a single row
            self.grid.append(tokens)

            line = file.readline()

            # replace \n with nothing
            line = line.replace("\n", "")

        # return the grid
        return self.grid

    def search_from(self, row, col):
        """recursive function to search the grid for the end (E)"""

        self.steps += 1

        # make sure row and col are valid points on the grid
        if row < 0 or col < 0 or row == len(self.grid) or col == len(self.grid[0]):
            # return False if not valid
            return False

        # check that the grid cell at row and col is not obstacle, tried, or deadend
        if (
            self.grid[row][col] == "X"
            or self.grid[row][col] == "T"
            or self.grid[row][col] == "D"
        ):
            # return False if obstacle, tried, or deadend
            return False

        # If end is found at row, col return True
        if self.grid[row][col] == "E":
            return True

        # If the cell at row, col is not the start cell, mark the cell as tried (T)
        if self.grid[row][col] != "S":
            self.grid[row][col] = "T"

        # draw the grid
        self.draw_grid()

        # pause the program for a short duration, try 0.5 and 0.01 seconds
        time.sleep(0.25)

        # recursively search differnt directions adjacent to current row, col (up, down, left, right)
        found = (
            self.search_from(row - 1, col)
            or self.search_from(row + 1, col)
            or self.search_from(row, col - 1)
            or self.search_from(row, col + 1)
        )

        # if any of the 4 directions returns True, mark the cel at row, col as part of the path and return True
        if found and self.grid[row][col] != "S":
            self.grid[row][col] = "P"
            return True
        # else, if the cell at row, col is not the start cell (S), mark it as a deadend
        elif self.grid[row][col] != "S":
            self.grid[row][col] = "D"

    def main(self):
        """reads a maze file and sets the search parameters"""

        # read maze file and create playground grid
        playground = self.read_grid()

        # find start position
        row, col = self.find_start()
        print(row)
        print(col)

        # call the search function, it takes the grid, row, column, and steps
        self.search_from(row, col)

        # create a list of tuples representing the path
        path = []
        for row in range(len(playground)):
            for col in range(len(playground[0])):
                if playground[row][col] == "P":
                    path.append((row, col))

        # print path length
        print("path length:", len(path))

        # draw the final grid
        self.draw_grid()

        # pause the grid drawing for 4 seconds
        time.sleep(4)

        # print the number of steps taken to find the path
        print("number of steps taken to reach answer:", self.steps)


if __name__ == "__main__":

    the_game = MazeGame()
    the_game.main()
