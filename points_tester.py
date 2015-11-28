__author__ = 'jens_e'


from coordinate import *
import math
import random
import matplotlib.pyplot as plt
import numpy as np


#fout=open('DAC_shiftreg/shiftregDAC/test.ino', 'w')

n=31
print "N is %d" %n
c=Square(100, 100, 100,100, n)
print "%s has %d points" %(c.get_shape_type(), c.get_n_points())
print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(c.min_x, c.max_x, c.min_y, c.max_y)
s = Shape(127,127, shape_type='complex')
for p in c.get_points():
    sc = Circle(p.get_x(), p.get_y(), 32, 4)
    s.add_points(sc.get_points())

print "%s has %d points" %(s.get_shape_type(), s.get_n_points())
print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(s.min_x, s.max_x, s.min_y, s.max_y)





#Z = np.logical_or(c.get_points_as_numpy_array(), s.get_points_as_numpy_array())
Z = c.get_points_as_numpy_array()
G = np.zeros((256,256,3))
G[Z>0.5] = [0,1,0]
G[Z<0.5] = [0,0,0]

plt.imshow(G)
plt.gca().invert_yaxis()
plt.show()
#fout.write(sq+ci)