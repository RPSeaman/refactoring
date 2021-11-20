'''
Will Johnson
CS151
Better Shape lib
27 February 2019
'''

import turtle as t
import random as r 

#t.tracer(False)
t.speed(0)
def goto(x,y):
	'''
	This is a function will take in both x and y parameters 
	'''
	t.up()
	t.goto(x,y)
	t.down()
		
def background():
	'''
	This is going to make the interior of a room i.e. wall and floor and one window
	'''
	goto(-500,500)
	t.begin_fill()
	t.color("white")
	for i in range (4):
		t.forward(1000)
		t.right(90)
	t.end_fill()
	t.color("brown")
	t.begin_fill()
	goto(-500,-100)
	for i in range(4):
		t.forward(1000)
		t.right(90)
	t.end_fill()
	
	
def painting(x,y,height,width,color,scale):
	'''
	This is going to draw a painting of different color and different size anywhere I want
	'''
	goto(x,y)
	t.color("gold")
	t.begin_fill()
	for i in range(2):
		t.forward(width*scale)
		t.right(90)
		t.forward(height*scale)
		t.right(90)
	t.end_fill()
	goto(x+5*scale,y-5*scale)
	t.color(color)
	t.begin_fill()
	for i in range (2):
		t.forward(width*scale-10*scale)
		t.right(90)
		t.forward(height*scale-10*scale)
		t.right(90)
	t.end_fill()
	
	
	
def block(x,y,width,height,color1,color2, fill = True):
	'''
	this is a function used to draw a rectangle at any space at any size and
	any color
	'''
	goto(x,y)
	t.color(color1,color2)
	if fill == True:
		t.begin_fill()
	for i in range(2):
		t.forward(width)
		t.right(90)
		t.forward(height)
		t.right(90)
	if fill == True:
		t.end_fill()
	
def sculpture(x,y,scale):
	'''
	this is going to call the clock function multiple times and allow me to draw a bunch
	of blocks all together at any size or location while remaining in scale
	'''
	block(x,y,45*scale, 90*scale,"Black")
	block(x+15*scale,y+30*scale,15*scale,30*scale,"white")
	block(x+20*scale,y+45*scale,5*scale,15*scale,"black")
	
	
def circle(x,y,color1,color2,scale, fill = True):
	'''This function allows me to make a circle at the size and color I want'''
	goto(x,y)
	t.color(color1,color2)
	if fill == True:
		t.begin_fill()
	for i in range(360):
		t.forward(1*scale)
		t.right(1)
	if fill == True:
		t.end_fill()
	
def testShapes():
	'''This calls my better shapes to make sure they run with new code'''
	block(-100,100,100,50,"Black","red")
	block(-100,300,100,50,"Black","red",False)
	circle(100,-100,"blue","red",1)
	circle(-100,-100,"blue","red",1,False)
	
def statue(x,y,scale):
	'''Draws a little statue on a block pedistal'''
	block(x,y,200*scale,50*scale,"Gold","Gold")
	circle(x+100*scale,y+115*scale,"gray","gray",scale)


def letter_D(x,y,scale,color1,color2,side,fill=True):
	''' This function just draws a letter d with fill defaulted'''
	goto(x,y)
	t.color(color1,color2)
	if fill == True:
		t.begin_fill()
	for i in range(180):
		t.forward(1*scale)
		t.right(1)
	t.right(90)
	t.forward(side*scale)
	if fill == True:
		t.end_fill()
		
		
def bunchOfCircles():
	'''This is a function that calls a bunch of circles at random spots in a range'''
	for i in range (10):
			circle(r.randint(-150,-30),r.randint(100,240),"black","black",r.randint(1,2),False)
	
#input("Enter")