__author__ = 'jens_e'

'''
A super quick script to generate X&Y coodinates for drawing a square on an oscilloscope with two 8-bit DACs,
so that the coordinates can be copypasted directly in to an Arduino sketch.
'''

points=360
x=[]
y=[]

f = open('squareCoord.txt',mode='w')

def squareWriter(points, xlist, ylist):
    for i in range(0,255,points/4):



f.write('byte shapeX[] = {')

for i in range(0,255,8):
        f.write(str(i)+', ')

for i in range(0,255,8):
        f.write(str(255)+', ')

for i in range(255,0,-8):
        f.write(str(i)+', ')

for i in range(255,0,-8):
        f.write(str(0)+', ')


f.write('\nbyte shapeY[] = {')

for i in range(0,255,8):
        f.write(str(0)+', ')

for i in range(0,255,8):
        f.write(str(i)+', ')

for i in range(255,0,-8):
        f.write(str(255)+', ')

for i in range(255,0,-8):
        f.write(str(i)+', ')

f.close()
