'''Will Johnson
9/27/18
task.py'''

import turtle as t
import random as r
import sys
import better_shapelib as bsl

def window(x,y):
#draws a window on the wall through which we see the desert
	bsl.goto(x,y)
	t.forward(400)
	t.right(90)
	t.forward(310)
	t.right(90)
	t.forward(400)
	t.right(90)
	t.forward(310)
	t.backward(155)
	t.right(90)

def door(x,y):
#draws a door
	t.color('brown')
	bsl.goto(x,y)
	t.forward(800)
	t.backward(800)
	t.left(90)
	t.forward(400)
	t.backward(400)
	bsl.goto(x+30,y-500)
	t.left(90)
	t.color('yellow')
	t.begin_fill()
	for i in range(360):
		t.forward((1/2))
		t.right(1)
	t.end_fill()


t.tracer(False)
window(-300,330)
bsl.desert1(-100,200,1,True,sys.argv[1],sys.argv[2])
door(150,350)
print(input('Enter'))