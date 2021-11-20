''' William Johnson
9/19/18
lab3.py'''

import turtle
import random
import sys


def star(x, y, size):
	turtle.up()
	turtle.goto(x, y)
	turtle.down()
	turtle.begin_fill()
	for i in range(5):
		turtle.forward(size)
		turtle.left(144)
	turtle.end_fill()

def star2(rays, size):
	for i in range(rays):
		turtle.down()
		turtle.setheading (i*360/rays)
		turtle.color(random.randint(0,1), random.randint(0,1), random.randint(0,1))
		turtle.forward(size)
		turtle.backward(size)
		turtle.up()

def main():
	turtle.tracer(False)
	turtle.color( 0.7, 0.7, 0.2 )
	N = 1000
	for i in range( N ):
		star( random.randint(-400, 400), random.randint(-400, 400), random.randint(5, 15) )

	turtle.update()
	if len(sys.argv)>=2:
		rays=int(sys.argv[1])
	else:
		rays = 10
	turtle.speed(0)
	for i in range(3):
		turtle.goto(random.randint(-400,400),random.randint(-400,400))
		star2(rays,100)

if __name__ == "__main__":
	main()
input('Enter')