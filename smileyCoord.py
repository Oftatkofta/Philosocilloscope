__author__ = 'jens_e'

import math

'''
A super quick script to generate X&Y coodinates for drawing a crude smiley on an oscilloscope with two 8-bit DACs,
so that the coordinates can be copypasted directly in to an Arduino sketch.
'''

f = open('smileyCoord.txt',mode='w')


def drawCircle(degrees, center, radius, coordinatefile):
    """
    Function to generate coorinates for a circle centered at center
     degrees = int (in degrees)
     center = int
     radius = int

    """

    f.write('byte shapeX[] = {')

    for i in range(0,degrees,2):
        alpha=math.radians(i)
        x = int(radius*math.cos(alpha)+center)
        coordinatefile.write(str(x)+', ')

    f.write('\nbyte shapeY[] = {')

    for i in range(0,360,2):
        alpha=math.radians(i)
        y = int(radius*math.sin(alpha)+center)

        f.write(str(y)+', ')

f.close()

