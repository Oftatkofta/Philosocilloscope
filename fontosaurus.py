from __future__ import print_function, division
from shapes import *

class Letter(Shape):
    def __init__(self, center_point, width, height, npoints):
        Shape.__init__(self, center_point, npoints, 'Letter')
        self.width = width
        self.heigth = height

class A(Letter):
    #TODO why is l3 off?
    def __init__(self, center_point, width, height, npoints):
        Letter.__init__(self, center_point, width, height, npoints)
        self.__coordgen()

    def __coordgen(self):
        p0 = Point(self.x-self.width/2.0, self.y-self.heigth/2.0)
        p1 = Point(self.x, self.y+self.heigth/2.0)
        p2 = Point(self.x+self.width/2.0, self.y-self.heigth/2.0)
        l1 = Line(p0, p1, self.npoints/3)
        l2 = Line(p1, p2, self.npoints/3)

        l3 = Line(l2.get_center_point(), l1.get_center_point(), self.npoints/3)
        print(l1, l2, l3)
        a = l1+l2+l3
        print(a)
        self.add_points(a.points)

