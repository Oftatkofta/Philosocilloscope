__author__ = 'jens_e'
"""
MR = GPOI18; Master Clear, active low
DS = GPIO17; Serial data input
OE = GPIO27; Output Enable, active low
ST_CP = GPIO22; latch
SH_CP = GPIO4; clock
"""

from shapes import *
from copy import *
import math
from random import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from fontosaurus import *

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

def rotate_tester(degrees, nshapes):


    s0 = Square(center, 75, 150,100)
    s0.set_origin_point(p1)
    s=deepcopy(s0)
    for i in range(nshapes):
        s1 = deepcopy(s0)
        s1.rotate2(math.radians(degrees))
        s += s1
        degrees+=degrees

    #s.scale(1.5,1)
    s.draw()

def a_teter(width, height, ppa, alpha):
    w=0
    o=Shape()
    while w<255:
        p=A(Point(w, 127), width, height, ppa)
        p.rotate(alpha*w)
        o+=p
        w+=width
    o.draw()

#a_teter(150,200, 40, math.pi/18)
rotate_tester(1,50)
