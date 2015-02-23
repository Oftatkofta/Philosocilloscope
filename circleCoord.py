import math

'''
A super quick script to generate X&Y coodinates for drawing a circle on an oscilloscope with two 8-bit DACs,
so that the coordinates can be copypasted directly in to an Arduino sketch.
'''
points=20
x=[]
y=[]

f = open('circleCoord.txt',mode='w')

def coordgen(pointnum, xlist, ylist):
    for i in range(0,360,360/pointnum):
        alpha=math.radians(i)
        xlist.append(int(128*math.cos(alpha)+127.5))
        ylist.append(int(128*math.sin(alpha)+127.5))

    f.write('byte shapeX[] = {')

    for i in range(0,len(xlist)):

        f.write(str(xlist[i])+', ')
    if i == len(xlist)-1:
        f.write(str(xlist[i])+'};\n')

    f.write('byte shapeY[] = {')

    for i in range(0,len(ylist)):

        f.write(str(ylist[i])+', ')
    if i == len(ylist)-1:
        f.write(str(xlist[i])+'};\n')

    f.close()

coordgen(points,x,y)
