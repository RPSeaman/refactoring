'''
Will Johnson
Lab3_2
CS151
Do the lab 3 idk
'''
import turtle as t
import random as r 

t.tracer(False)
t.pensize(4)
t.colormode(255)

def goto(x,y):
	'''
	This is a function will take in both x and y parameters 
	'''
	t.up()
	t.goto(x,y)
	t.down()

def block(x,y,width,height,color2,scale, fill = True):
	'''
	this is a function used to draw a rectangle at any space at any size and
	any color
	'''
	goto(x,y)
	t.color("black",color2)
	if fill == True:
		t.begin_fill()
	for i in range(2):
		t.forward(width*scale)
		t.right(90)
		t.forward(height*scale)
		t.right(90)
	if fill == True:
		t.end_fill()

def main():
	for i in range (200):
		temp = r.randint(0,100)
		if temp < 40:
			bool = True
		else:
			bool = False

		block(r.randint(-500,500),r.randint(-500,500),r.randint(50,100),r.randint(50,100), (r.randint(0,255),r.randint(0,255),r.randint(0,255)),r.randint(0,3),bool)
		

if __name__ == '__main__':
	main()


input("Enter")