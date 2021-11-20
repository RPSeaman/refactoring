''' Will Johnson
CS 151 Fall
better shape library for project 3'''


#this simply is there to import the needed info from turtle random and sys
import turtle as t
import sys
import random as r


def goto(x,y):

#This function is just meant to move
#	the turtel without leaving a mark
#	Parameters:
#	x: hoirzontal location
#	y: vertical location
	
	print('goto(): going to', x,y)
	t.penup()
	t.goto(x,y)
	t.pendown()
	
def block(width,height,scale,fill):

#This function tells turtle t go to a specific area and begin to draw a block

	
	print('block(): drawing block of size',width,height)
	t. color('dark green')
	if (fill == True):
		t.begin_fill()
		for i in range(2):
			t.forward(height)
			t.left(90)
			t.forward(width)
			t.left(90)
		t.end_fill()
	else:
		for i in range(2):
			t.forward(height)
			t.left(90)
			t.forward(width)
			t.left(90)

def hexagon(x,y,sidelength,fill,color2):
	#thiS makes a hexagon
	#x is x coordinate
	#y is y coordinate
	#sidelength is the length each 6 sides
	#the fill function simply lets me decide if I want to fill the function or not 
	print('this is a hexagon')
	if fill == True:
		goto(x,y)
		t. color(color2)
		t.begin_fill()
		for i in range(6):
			t.forward(sidelength)
			t.right(60)
		t.end_fill()
	else:
		goto(x,y)
		t. color('firebrick')
		for i in range(6):
			t.forward(sidelength)
			t.right(60)

def octagonDraw(x,y,sidelength,fill,color2):
	#thiS makes a hexagon
	#x is x coordinate
	#y is y coordinate
	#sidelength is the length each 8 sides
	print('this is an octagon')
	goto(x,y)
	if fill == True:
		t. color(color2)
		t.begin_fill()
		for i in range(8):
			t.forward(sidelength)
			t.right(360/8)
		t.end_fill()
	else:
		t. color('firebrick')
		for i in range(8):
			t.forward(sidelength)
			t.right(360/8)

def tmblweed(x,y,sidelength,scale,fill):
#This is a function simply making a 20 sided polygon and filling it to look like a 
#thing of tumbleweed
	goto(x,y)
	if fill==True:
		t.color('snow4')
		t.begin_fill()
		for i in range(20):
			t.forward(sidelength*scale)
			t.right(360/20)
		t.end_fill()
	else:
		t.color('snow4')
		for i in range(20):
			t.forward(sidelength*scale)
			t.right(360/20)
			
def cactus(x,y,scale,fill):
	#this is a function made to make a cactus with a block and a semi circle
	#Parameters:
	#	X: x coordinate 
	#	Y: y coordinate
	#scale controls the scale of the cactus
	goto(x,y)
	if fill == True:
		t.begin_fill()
		t.color('dark green')
		block(200*scale,30*scale,scale,fill)
		t.color('dark green')
		t.left(90)
		t.forward(200*scale)
		for i in range(int(45*scale)):
			t.forward(1)
			t.right(4/scale)
		t.end_fill()
	else:
		t.color('dark green')
		block(200*scale,30*scale,scale,fill)
		t.left(90)
		t.forward(200*scale)
		for i in range(int(45*scale)):
			t.forward(1)
			t.right(4/scale)

def desertSand(x,y,scale,color):
	goto(x,y)
	t.color(color)
	t.forward(400*scale)
			
def desert1(x,y,scale,fill,color,color2):
#this function simply is calling to shapelib and using the functions below to make my
#background, cacti, and the simples shapes acting as rocks and the tumble weed
	if len(sys.argv)>1:
		t.color(sys.argv[1])
		desertSand(x-200*scale,y+scale,scale,color)
		cactus(x+40*scale,y-100*scale,scale,fill)
		t.left(90)
		cactus(x-100*scale,y-100*scale,scale,fill)
		t.color(color2)
		hexagon(x+scale,y-50*scale,35*scale,fill,color2)
		t.color(color2)
		octagonDraw(x-50*scale,y-100*scale,10*scale,fill,color2)
		tmblweed(x+150*scale,y-100*scale,5*scale,scale,fill)
	else:
		t.color(sys.argv[1])
		desertSand(x-200*scale,y+scale,'light goldenrod')
		cactus(x+40*scale,y-100*scale,scale,fill)
		t.left(90)
		cactus(x-100*scale,y-100*scale,scale,fill)
		t.color('firebrick')
		hexagon(x+scale,y-50*scale,35*scale,fill)
		octagonDraw(x-50*scale,y-100*scale,10*scale,fill)
		t.color('snow4')
		tmblweed(x+150*scale,y-100*scale,5*scale,scale,fill)
