from __future__ import print_function, division
from shapes import *

class Letter(Shape):
    def __init__(self, center_point, width, height, npoints):
        Shape.__init__(self, center_point, npoints, 'Letter')
        self.width = width
        self.heigth = height

class A(Letter):

    def __init__(self, center_point, width, height, npoints,
                 relativeCrossbarHeight=0.45, relativeCrossbarPoints=0.15):
        Letter.__init__(self, center_point, width, height, npoints)
        self.relativeCrossbarHeight = relativeCrossbarHeight
        self.relativeCrossbarPoints = relativeCrossbarPoints
        self.__coordgen()

    def __coordgen(self):

        # Points in the bottom corners and top center of bounding box
        pBottomLeft = Point(self.x-self.width/2.0, self.y-self.heigth/2.0)
        pTopCenter = Point(self.x, self.y+self.heigth/2.0)
        pBottomRight = Point(self.x+self.width/2.0, self.y-self.heigth/2.0)


        # Number of points per side line
        linePoints = int(self.npoints * ((1 -self.relativeCrossbarPoints) / 2))

        # Lines from bottom corners to top center
        l1 = Line(pBottomLeft, pTopCenter, npoints=linePoints)
        l2 = Line(pTopCenter, pBottomRight, npoints=linePoints)

        #Line across l1 & l2 to form brossbar at relative height from bottom
        p0_x = l1.min_x + (self.relativeCrossbarHeight * self.width / 2.0)
        p0_y = l1.min_y + (self.heigth * self.relativeCrossbarHeight)
        p1_x = l2.max_x - (self.relativeCrossbarHeight * self.width / 2.0)
        p0 = Point(p0_x, p0_y)
        p1 = Point(p1_x, p0_y)
        l3 = Line(p0, p1, npoints=self.npoints - 2*linePoints)

        a = l1+l2+l3

        self.add_points(a.points, recalculateCenterPoint=False)
        #self._recalculate_centerPoint()
        print(a)

