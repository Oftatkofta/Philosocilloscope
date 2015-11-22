import math
import string
import numpy as np


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

    def get_x(self):
        """
        Getter method for a Coordinate object's x coordinate.
        """
        return self.x

    def get_y(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.get_x()) + ',' + str(self.get_y()) + '>'

    def __eq__(self, other):
        if (self.get_x() == other.get_x()) and (self.get_y() == other.get_y()):
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

    def get_n_points(self):

        return len(self.points)

    def add_point(self, point):

        self.points.append(point)

        if self.get_n_points() == 1:
            self.max_x, self.min_x = point.get_x(), point.get_x()
            self.max_y, self.min_y = point.get_y(), point.get_y()

        if point.get_x() > self.max_x:
            self.max_x = point.get_x()

        if point.get_y() > self.max_y:
            self.max_y = point.get_y()

        if point.get_x() < self.min_x:
            self.min_x = point.get_x()

        if point.get_y() < self.min_y:
            self.min_y = point.get_y()

        self.points.append(pointlist)
    def add_points(self, pointlist):

    def get_shape_type(self):
        return self.shape_type

    def get_points(self):
        """

        :return: (list) pointlist
        """
        return self.points

    def get_sorted_points(self):
        """
        :return:
        (list) Points sorted on distance from Origo (0,0)
        """

        return sorted(self.points, key=lambda point: math.sqrt(point.x ** 2 + point.y ** 2))

    def sort_points(self):
        """ Sorts the pointlist in place on distance from Origo (0,0)
        :return:
        None
        """
        self.points.sort(key=lambda point: math.sqrt(point.x ** 2 + point.y ** 2))

    def get_points_as_C_array(self, variablename, ):
        """

        :return: (str) Points as a C-array consisting of 16-bit words with x as MSB ends with newline
        """
        out = "uint16_t %s[] = {" %variablename
        for point in self.get_sorted_points():
            "Constrains values to 8-bit"
            x = max(min(int(round(point.get_x())), 255), 0)
            y = max(min(int(round(point.get_y())), 255), 0)
            out += str((x << 8) + y) + ', '
        out = string.rstrip(out,', ')
        return out + '};\n'

    def get_points_as_numpy_array(self):


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
            self.add_point(Point(x, y))
            alpha += alpha


class Square(Shape):
    def __init__(self, center_x, center_y, width, heigth, npoints):
        Shape.__init__(self, center_x, center_y, npoints, 'square')
        self.width = width
        self.height = heigth
        self._coordgen()

    def _coordgen(self):
        """
        Adds roughly

        """
        #TODO make npoints exact!
        #Calculate corner points
        x0, x1 = self.x-self.width*0.5, self.x+self.width*0.5
        y0, y1 =self.y-self.height*0.5, self.y+self.height*0.5
        #Calculate number of points per side, rounds to nearest whole number
        n_hpoints=round(float(self.width)/(self.width+self.height)*0.5*self.npoints)
        n_vpoints=round(float(self.height)/(self.width+self.height)*0.5*self.npoints)
        #Calculate distnce between points
        dx, dy =self.width/n_hpoints, self.height/n_vpoints

        xlist=[]
        ylist=[]
        for i in range(int(n_hpoints)):
            x = x0+i*dx
            if x > x1:
                break
            xlist.append(Point(x, y0))
            xlist.append(Point(x, y1))


        for i in range(int(n_vpoints)):
            y=y0+i*dy
            if y > y1:
                break
            ylist.append(Point(x0, y0+i*dx))
            ylist.append(Point(x1, y0+i*dy))

        self.points = self.points+xlist+ylist


