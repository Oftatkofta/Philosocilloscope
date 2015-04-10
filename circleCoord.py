import math

'''
A super quick script to generate X&Y coodinates for drawing a circle on an oscilloscope with two 8-bit DACs,
so that the coordinates can be copypasted directly in to an Arduino sketch.
'''
origo=(127.5,127.5)
radius=128
xl=[]
yl=[]

f = open('circleCoord.txt',mode='w')

def coordgen(pointnum, xlist, ylist, radius, origo):
    for i in range(0,360,360/pointnum):
        alpha=math.radians(i)
        x=int(radius*math.cos(alpha)+origo[0])
        y=int(radius*math.sin(alpha)+origo[1])
        xlist.append(x)
        ylist.append(y)


def coordwriter(infile, xlist, ylist):
    infile.write('byte shapeX[] = {')

    for i in range(0,len(xlist)):

        infile.write(str(xlist[i])+', ')
    if i == len(xlist)-1:
        infile.write(str(xlist[i])+'};\n')

    infile.write('byte shapeY[] = {')

    for i in range(0,len(ylist)):

        infile.write(str(ylist[i])+', ')
    if i == len(ylist)-1:
        infile.write(str(xlist[i])+'};\n')

    infile.close()

for i in range(radius, 10, -20):
    coordgen(i, xl,yl, i, origo)
for i in range(10, radius, 20):
    coordgen(i, xl,yl, i, origo)



coordwriter(f, xl, yl)
