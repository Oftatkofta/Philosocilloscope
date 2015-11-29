__author__ = 'jens_e'


from coordinate import *
import math
import random
import matplotlib.pyplot as plt
import numpy as np


#fout=open('DAC_shiftreg/shiftregDAC/test.ino', 'w')

n=64
print "N is %d" %n
c=Square(100, 100, 123,100, n)
print "%s has %d points" %(c.get_shape_type(), c.get_n_points())
print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(c.min_x, c.max_x, c.min_y, c.max_y)
s = Shape(127,127, shape_type='complex')
for p in c.get_points():
    sc = Circle(p.get_x(), p.get_y(),random.randint(1,30), 33)
    s.add_points(sc.get_points())

print "%s has %d points" %(s.get_shape_type(), s.get_n_points())
print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(s.min_x, s.max_x, s.min_y, s.max_y)





#Z = np.logical_or(c.get_points_as_numpy_array(), s.get_points_as_numpy_array())
#s.draw()
s.draw()
#fout.write(sq+ci)