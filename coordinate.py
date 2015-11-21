__author__ = 'jens_e'
import math
import string


class Point(object):
    """
    Class that represents an X/Y coordinate pair.



    Args:
        X (int or float): X-coorinate.
        Y (int or float): Y-coordinate.

    Attributes:
        X.
        Y.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        """
        Getter method for a Coordinate object's x coordinate.
        """
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        if (self.getX() == other.getX()) and (self.getY() == other.getY()):
            return True
        return False

    def __repr__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'


class Shape(Point):
    def __init__(self, center_x, center_y, npoints=0, shape_type='NA'):
        Point.__init__(self, center_x, center_y)
        self.shape_type = shape_type
        self.points = []
        self.npoints = int(npoints)
        self.max_x = None
        self.min_x = None
        self.max_y = None
        self.min_y = None

    def __repr__(self):
        return 'Shape at(' + str(self.x) + ', ' + str(self.y) + ')'

    def getNpoints(self):

        return len(self.points)

    def addPoint(self, point):

        self.points.append(point)

        if self.getNpoints() == 1:
            self.max_x, self.min_x = point.getX(), point.getX()
            self.max_y, self.min_y = point.getY(), point.getY()

        if point.getX() > self.max_x:
            self.max_x = point.getX()

        if point.getY() > self.max_y:
            self.max_y = point.getY()

        if point.getX() < self.min_x:
            self.min_x = point.getX()

        if point.getY() < self.min_y:
            self.min_y = point.getY()

    def addPoints(self, pointlist):
        self.points.append(pointlist)

    def getShapeType(self):
        return self.shape_type

    def getPoints(self):
        return self.points

    def getSortedPoints(self):
        """
        :return: (list) Points sorted on distance from origo (0,0)
        """

        return sorted(self.points, key=lambda point: math.sqrt(point.x ** 2 + point.y ** 2))

    def sortPoints(self):
        """
        Sorts the pointlist in place
        :return:
        None
        """
        self.points.sort(key=lambda point: math.sqrt(point.x ** 2 + point.y ** 2))

    def getPointsAsArray(self, variablename, ):
        """

        :return: (str) Points as a C-array consisting of 16-bit words with x as MSB
        """
        out = "uint16_t %s[] = {" %variablename
        for point in self.getSortedPoints():
            "Constrains values to 8-bit"
            x = max(min(int(round(point.getX())), 255), 0)
            y = max(min(int(round(point.getY())), 255), 0)
            out += str((x << 8) + y) + ', '
        out = string.rstrip(out,', ')
        return out + '};'


class Circle(Shape):
    def __init__(self, origo_x, origo_y, radius, npoints):
        Shape.__init__(self, origo_x, origo_y, npoints, 'circle')
        self.radius = radius
        self._coordgen()

    def _coordgen(self):

        if self.npoints > 1000:
            alpha = long(2L * math.pi / self.npoints)
        else:
            alpha = float(2 * math.pi / self.npoints)

        for i in range(self.npoints):
            x = self.radius * math.cos(alpha) + self.x
            y = self.radius * math.sin(alpha) + self.y
            self.addPoint(Point(x, y))
            alpha += alpha


class Square(Shape):
    def __init__(self, center_x, center_y, width, heigth, npoints):
        Shape.__init__(self, center_x, center_y, npoints, 'square')
        self.width = width
        self.height = heigth
        self._coordgen()

    def _coordgen(self):
        x0=self.x-self.width/2.0
        x1=self.x+self.width/2.0
        y0=self.y-self.height/2.0
        y1=self.y+self.height/2.0
        n_hpoints=int(round(float(self.width)/(self.width+self.height)*self.npoints))
        n_vpoints=int(round(float(self.height)/(self.width+self.height)*self.npoints))
        dx=self.width/(n_hpoints/2.0)
        dy=self.height/(n_vpoints/2.0)

        for i in range(n_hpoints/2):
            x = x0+i*dx
            p0 = Point(x, y0)
            p1 = Point(x, y1)
            self.addPoint(p0)
            self.addPoint(p1)

        for i in range(n_vpoints/2):
            y=y0+i*dy
            p0 = Point(x0, y0+i*dx)
            p1 = Point(x1, y0+i*dy)
            self.addPoint(p0)
            self.addPoint(p1)