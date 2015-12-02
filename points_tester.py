__author__ = 'jens_e'


from coordinate import *
from copy import *
import math
import random
import matplotlib.pyplot as plt
import numpy as np


#fout=open('DAC_shiftreg/shiftregDAC/test.ino', 'w')

n=7
center = Point(127,127)
print "N is %d" %n
c=Circle(center,50,n)
o=Circle(center, 100, n)
print "%s has %d points" %(c.get_shape_type(), c.get_n_points())
print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(c.min_x, c.max_x, c.min_y, c.max_y)
l = Shape(center, shape_type='complex')
for i in range(c.get_n_points()):
    p0 = c.points[i]
    p1 = o.points[i]
    ls = Line(p0, p1, 30)
    poop = Circle(p1, 10,20)
    loop= Square(p0, 10,12, 31)
    l.add_points(ls.get_points()+poop.get_points()+loop.get_points())



print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(l.min_x, l.max_x, l.min_y, l.max_y)
#
# w = Shape(250,250, shape_type='wierd')
# alpha = 6 * math.pi / n
# radius = 50
# for i in range(n):
#     radius += random.randint(-1,10)
#     x = radius *  math.cos(alpha*i) + w.get_x()
#     y = radius *  math.sin(alpha*i) + w.get_y()
#     w.add_point(Point(x, y))
#
# s = Shape(250,250, shape_type='complex')
# for p in w.get_points():
#     sc = Square(p.get_x(), p.get_y(),random.randint(1,90), random.randint(1,90),33)
#     s.add_points(sc.get_points())
#     for p1 in sc.get_points():
#         ci = Circle(p1.get_x(), p1.get_y(),random.randint(10,30), random.randint(5,20))
#         s.add_points(ci.get_points())


#Z = np.logical_or(c.get_points_as_numpy_array(), s.get_points_as_numpy_array())
#s.draw()
#l = Circle(center, 70, 99)
print "%s has %d points" %(l.get_shape_type(), l.get_n_points())
print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(l.min_x, l.max_x, l.min_y, l.max_y)
testpoints = [copy(center),Point(150,150), Point(63,63), Point(50,50), Point(1,1), center]
for p in testpoints:
    l.translate(p)
    print "%s has %d points" %(l.get_shape_type(), l.get_n_points())
    print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(l.min_x, l.max_x, l.min_y, l.max_y)
    l.draw()
#fout.write(sq+ci)