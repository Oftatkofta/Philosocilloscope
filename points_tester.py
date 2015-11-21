__author__ = 'jens_e'


from coordinate import *
import math
import random

#fout=open('DAC_shiftreg/shiftregDAC/test.ino', 'w')


c=Circle(128, 128, 100, 100)
s=Square(128,128,45,90,100)
print "%s has %d points" %(s.getShapeType(), s.getNpoints())
print "minX: %s, maxX: %s, minY: %s, maxY: %s" %(s.min_x, s.max_x, s.min_y, s.max_y)

print s.points
print s.getSortedPoints()
print s.getPointsAsArray('test')

#fout.write()