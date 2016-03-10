__author__ = 'jens_e'


from coordinate import *
from copy import *
import math
from random import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


#fout=open('DAC_shiftreg/shiftregDAC/test.ino', 'w')

center = Point(127,127)
p0 = Point(0,0)
p1 = Point(0,255)
p2 = Point(255, 255)
p3 = Point(255, 0)

def funkyFunction():
    p0 = Point(0,0)
    p1 = Point(0,255)
    p2 = Point(255, 255)
    p3 = Point(255, 0)

    p4 = Point(0,127)
    p5 = Point(127,255)
    p6 = Point(255, 127)
    p7 = Point(127,0)


    l1 = Line(p1,p2,20)
    l2 = Line(p0,p3,20)
    l3 = Line(p0,p1,20)
    l4 = Line(p3,p2,20)

    l=l1+l2+l3+l4

    for i in range(l1.get_n_points()):
            p0=l1.points[i]
            p1 = l3.points[i]
            p2 = l4.points[i]
            p3=l2.points[i]
            b1 = Bezier(p0, p4, p5, p3, 100)
            b2 = Bezier(p1, p6, p7, p2, 100)
            l += (b1+b2)

    print "%s has %d points" %(l.get_shape_type(), l.get_n_points())
    print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(l.min_x, l.max_x, l.min_y, l.max_y)
    l.draw()

#binaryNumpyArrayToPoints(f.get_points_as_numpy_array())

def beziercle():
    p0 = Point(0,0)
    p1 = Point(0,255)
    p2 = Point(255, 255)
    p3 = Point(255, 0)

    c = Bezier(p0,p3,p1,p2, 13)
    o = Shape(center)

    b = Square(center,123,45,79)
    t=c.get_points()
    for i in xrange(1,c.get_n_points()-4):

        b = Bezier(t[i+1], t[i], t[i+3], t[i+2],10)

        o += b
    o.draw()

def rotate_tester(degrees):

    l = Square(center, 45, 150, 67)
    s = Square(center, 45, 150, 67)
    s.set_origin(center)
    l.set_origin(center)

    l.rotate(math.radians(degrees))
    s+=l

    s.draw()

c = Circle(center, 50, 33)
s = Square(center, 10, 10, 13)
l = Line(p0, p2, 13)

c = c * s + l

c.draw()
