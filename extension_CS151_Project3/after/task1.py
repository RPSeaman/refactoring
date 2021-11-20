'''William Johnson
9/27/18
task1.py'''

import turtle as t
import random as r
import sys
import better_shapelib as bsl



t.tracer(False)
bsl.desert1(-100,200,1,True)
t.left(85)
bsl.desert1(-300,-200,(1/2),False)
t.left(85)
bsl.desert1(150,-180,(3/2),True)

print(input('Press Enter to Continue'))