__author__ = 'jens_e'


from coordinate import *
import math
import random

fout=open('DAC_shiftreg/shiftregDAC/test.ino', 'w')

n=171
print "N is %d" %n
c=Circle(128, 128, 100, n)
print "%s has %d points" %(c.get_shape_type(), c.get_n_points())
print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(c.min_x, c.max_x, c.min_y, c.max_y)

s=Square(127,127,100,50,n)
print "%s has %d points" %(s.get_shape_type(), s.get_n_points())
print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(s.min_x, s.max_x, s.min_y, s.max_y)

print s.get_points()
print s.get_sorted_points()
s.sort_points()
sq = s.get_points_as_C_array('test1')
ci = c.get_points_as_C_array('test2')
fout.write(sq+ci)