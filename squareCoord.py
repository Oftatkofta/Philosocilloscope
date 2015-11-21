__author__ = 'jens_e'

'''
A super quick script to generate X&Y coodinates for drawing a square on an oscilloscope with two 8-bit DACs,
so that the coordinates can be copypasted directly in to an Arduino sketch.
'''

points=360
x=[]
y=[]

f = open('squareCoord.txt',mode='w')



for i in range(0,255,16):
    for j in range(0,255,16):
        x.append(i)
        y.append(j)


f.write('byte shapeX[] = {')
f.write(str(x))
f.write('\nbyte shapeY[] = {')
f.write(str(y))

f.close()
