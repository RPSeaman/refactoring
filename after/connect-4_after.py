"""
name: Ryan and John
file: connect-4_after.py
data: Nov 17, 2021
course: CS321
description: Refactoring Project
"""

import turtle


class TheGame:
    def __init__(self):
        self.window = self.make_window("Connect 4", "LightGoldenrod", 800, 600)
        self.my_turtle = self.make_turtle("classic", "white", 1, 1, 0, 0)
        self.grid = [[0] * 7 for _ in range(5)]
        self.x_offset = -150
        self.y_offset = 200
        self.tile_size = 50
        self.turn = 1
        self.colors = ["white", "red", "blue"]

    def make_window(self, window_title, bgcolor, width, height):
        window = turtle.getscreen()
        window.title(window_title)
        window.bgcolor(bgcolor)
        window.setup(width, height)
        window.tracer(0)
        return window

    def make_turtle(
        self, shape, color, stretch_width, stretch_length, x_position, y_position
    ):
        turt = turtle.Turtle()
        turt.speed(0)
        turt.shape(shape)
        turt.color(color)
        turt.shapesize(stretch_width, stretch_length)
        turt.penup()
        turt.goto(x_position, y_position)
        return turt

    def teleport(self, point: tuple):
        self.my_turtle.up()
        self.my_turtle.goto(*point)
        self.my_turtle.down()

    def draw_grid(self):
        self.teleport((self.x_offset, self.y_offset))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):

                self.teleport(
                    (
                        self.x_offset + col * self.tile_size,
                        self.y_offset - row * self.tile_size,
                    )
                )

                self.my_turtle.dot(self.tile_size - 5, self.colors[self.grid[row][col]])

    def row_win(self, player):
        for row in range(len(self.grid)):
            count = 0
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == player:
                    count += 1

                    if count == 4:
                        return True

    def col_win(self, player):
        for col in range(len(self.grid[0])):
            count = 0
            for row in range(len(self.grid)):
                if self.grid[row][col] == player:
                    count += 1

                    if count == 4:
                        return True

    def diag_win(self, player):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                if row + 3 < len(self.grid) and col + 3 < len(self.grid[row]):
                    if (
                        self.grid[row][col] == player
                        and self.grid[row + 1][col + 1] == player
                        and self.grid[row + 2][col + 2] == player
                        and self.grid[row + 3][col + 3] == player
                    ):
                        return True

        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                if row - 3 >= 0 and col + 3 < len(self.grid[row]):
                    if (
                        self.grid[row][col] == player
                        and self.grid[row - 1][col + 1] == player
                        and self.grid[row - 2][col + 2] == player
                        and self.grid[row - 3][col + 3] == player
                    ):
                        return True

    def is_win(self, player):
        col_win_check = self.col_win(player)
        row_win_check = self.row_win(player)
        diag_win_check = self.diag_win(player)

        if col_win_check == True or row_win_check == True or diag_win_check == True:
            return True

    def play(self, x_position, y_position):

        row = int(abs((y_position - self.y_offset - 25) // (50) + 1))
        col = int(abs((x_position - self.x_offset - 25) // (50) + 1))

        print(row, col)
        self.grid[row][col] = self.turn
        self.draw_grid()
        self.window.update()

        if self.is_win(1):
            print("player 1 won")

        elif self.is_win(2):
            print("player 2 won")

        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def main(self):
        self.window.onscreenclick(self.play)
        self.window.listen()
        self.draw_grid()

        while True:
            selected_row = int(input("enter row, player " + str(self.turn) + ": "))
            selected_col = int(input("enter col, player " + str(self.turn) + ": "))

            if self.grid[selected_row][selected_col] == 0:

                if self.turn == 1:
                    self.grid[selected_row][selected_col] = 1
                else:
                    self.grid[selected_row][selected_col] = 2

            self.draw_grid()
            self.window.update()


if __name__ == "__main__":
    the_game = TheGame()
    the_game.main()
