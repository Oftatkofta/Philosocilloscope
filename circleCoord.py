import math

'''
A super quick script to generate X&Y coodinates for drawing a circle on an oscilloscope with two 8-bit DACs,
so that the coordinates can be copypasted directly in to an Arduino sketch.
'''

f = open('circleCoord.txt',mode='w')

f.write('byte shapeX[] = {')

for i in range(0,360,2):
    alpha=math.radians(i)
    x = int(128*math.cos(alpha)+127.5)
    if i != 358:
        f.write(str(x)+', ')
    else:
        f.write(str(x)+'};\n')

f.write('byte shapeY[] = {')

for i in range(0,360,2):
    alpha=math.radians(i)
    y = int(128*math.sin(alpha)+127.5)
    if i != 358:
        f.write(str(y)+', ')
    else:
        f.write(str(y)+'};\n')

f.close()

