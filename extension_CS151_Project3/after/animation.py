'''
Will Johnson
Project 3
CS 151
27 February 2019
'''

import turtle as t 
import random as r 
import Better_shapelib_2 as bsl
import project3_2 as p

t.tracer(False)


def animation(x,y,scale):
	'''This function runs a simple animation'''
	for i in range(100):
		t.reset()
		p.main()
		t.right(90)
		bsl.statue(x+i*2,y,scale)
		t.update()
		
		
	
animation(-200,-250,.5)

input("Enter")