import math
import string
import numpy as np
import matplotlib.pyplot as plt
from copy import *


class Point(object):
    #TODO Add color to Point
    """
    Class that represents an X/Y coordinate pair.

    Args:
        X (int or float): X-coorinate.
        Y (int or float): Y-coordinate.

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

    def get_rounded_x(self):
        """
        :return:(int) x coordinate rounded to nearest whole number.
        """
        return int(round(self.x))

    def get_rounded_y(self):
        """
        :return: (int) y coordinate rounded to nearest whole number.
        """
        return int(round(self.y))

    def get_constrained_x(self, max_x = 255):
        """
        :return: (int) X-coodinate constrained to max_x, defaults to 8-bit
        range 0-255
        """
        return max(min(self.get_rounded_x(), max_x), 0)

    def get_constrained_y(self, max_y = 255):
        """
        :return: (int) Y-coodinate constrained to max_x, defaults to 8-bit
        range 0-255
        """
        return max(min(self.get_rounded_y(), max_y), 0)


    def __str__(self):
        return '<' + str(self.get_x()) + ',' + str(self.get_y()) + '>'

    def __eq__(self, other):
        if (self.get_x() == other.get_x()) and (self.get_y() == other.get_y()):
            return True
        return False

    def __repr__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'


class Shape(Point):
    def __init__(self, center_Point, npoints=0, shape_type='NA'):
        Point.__init__(self, center_Point.get_x(), center_Point.get_y())
        self.shape_type = shape_type
        self.points = []
        self.npoints = npoints
        self.max_x = None
        self.min_x = None
        self.max_y = None
        self.min_y = None
        self.centerPoint = center_Point

    def __repr__(self):
        return 'Shape centered at(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        #Combines two shapes in to one
        outPoints = self.points + other.points
        outMaxX = max(self.max_x, other.max_x)
        outMinX = min(self.min_x, other.min_x)
        outMaxY = max(self.max_y, other.max_y)
        outMinY = min(self.min_y, other.min_y)

        outCenter = Point(outMaxX-outMinX, outMaxY-outMinY)

        outShape = Shape(outCenter, len(outPoints), 'composite')

        outShape.max_x = outMaxX
        outShape.min_x = outMinX
        outShape.max_y = outMaxY
        outShape.min_y = outMinY
        outShape.points = outPoints

        return outShape


    def __mul__(self, other):

        self.shape_type = 'composite'

        out = deepcopy(self)

        for point in self.points:
            cop = deepcopy(other)
            cop.translate(point)
            out += cop

        return out



    def get_n_points(self):

        return len(self.points)

    def add_point(self, point):

        self.points.append(point)


        if self.max_x == None:
            self.max_x, self.min_x = point.get_x(), point.get_x()
            self.max_y, self.min_y = point.get_y(), point.get_y()
            self.centerPoint = point

        if point.get_x() > self.max_x:
            self.max_x = point.get_x()

        if point.get_y() > self.max_y:
            self.max_y = point.get_y()

        if point.get_x() < self.min_x:
            self.min_x = point.get_x()

        if point.get_y() < self.min_y:
            self.min_y = point.get_y()

    def add_points(self, pointlist):
        """
        :param pointlist: (list) list of Point objects to add to the shape
        :return: None
        """
        for point in pointlist:
            self.add_point(point)

    def get_center_point(self):
        """
        Returns: (Point) Centerpoint of Shape

        """
        return self.centerPoint

    def get_shape_type(self):
        """

        :return: (str) Type of shape
        """
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

        return sorted(self.points,
                      key=lambda point: math.sqrt(point.x ** 2 + point.y ** 2))

    def sort_points(self):
        """ Sorts the pointlist in place on distance from Origo (0,0)
        :return:
        None
        """
        self.points.sort(
            key=lambda point: math.sqrt(point.x ** 2 + point.y ** 2))

    def get_points_as_C_array(self, variablename):
        """

        :return: (str) Points as a C-array consisting of 16-bit words
        with x coordinate as MSB, and y as LSB ends with newline.

        Args:
            variablename: (str) Name of resulting C array
        """
        out = "uint16_t %s[] = {" %variablename
        for point in self.get_sorted_points():
            "Constrains values to 8-bit"
            x = point.get_constrained_x()
            y = point.get_constrained_y()
            out += str((x << 8) + y) + ', '
        out = string.rstrip(out,', ')
        return out + '};\n'

    def get_points_as_numpy_array(self, height=256, width=256):
        """

        Returns: (numpy array) a width x height array with binary numbers
        representing the shape on screen, xy coordinates are cropped
        to fit within the array, defaults to 8-bit range (0-255).

        """

        out = np.zeros((height,width),dtype = bool)
        for p in self.get_points():
            out[p.get_constrained_y(height-1), p.get_constrained_x(width-1)] = True
        return out

    def draw(self, height=256, width=256):
        """
        shows the shape as a pyplot
        Returns: (Pyplot)

        Args:
            width: (int) Canvas width in pixels
            height: (int) Canvas height in pixels

        """
        npArray = self.get_points_as_numpy_array(height, width)
        RGB = np.zeros(npArray.shape+(3,))

        RGB[npArray>0.5] = [0,1,0]
        RGB[npArray<0.5] = [0,0,0]
        plt.imshow(RGB)
        plt.gca().invert_yaxis()
        plt.show()

    def translate(self, newCenterPoint):
        """
        Translates all points around a new centerpoint.
        Args:
            newCenterPoint: (Point) move Shape center to this point

        Returns: (None)

        """
        dx = newCenterPoint.x - self.x
        dy = newCenterPoint.y - self.y

        self.centerPoint = newCenterPoint
        self.x += dx
        self.y += dy
        self.max_x += dx
        self.min_x += dx
        self.max_y += dy
        self.min_y += dy

        for point in self.points:
            point.x += dx
            point.y += dy

class Circle(Shape):

    def __init__(self, origo_Point, radius, npoints):
        Shape.__init__(self, origo_Point, npoints, 'circle')
        self.radius = radius
        self._coordgen()

    def _coordgen(self):
        """
        Adds equally spaced points along the perimeter of the to the circle
        counterclockwise.

        """
        alpha = 2 * math.pi / self.npoints

        for i in range(self.npoints):
            x = self.radius *  math.cos(alpha*i) + self.x
            y = self.radius *  math.sin(alpha*i) + self.y
            self.add_point(Point(x, y))


class Square(Shape):
    def __init__(self, center_Point, width, heigth, npoints):
        Shape.__init__(self, center_Point, npoints, 'square')
        self.width = width
        self.height = heigth
        self._coordgen()

    def _coordgen(self):
        """
        Adds equally spaced points in a clockwise fashion starting from the
        bottom left corner.

        """
        #TODO Make fix upper left corner point skip bug

        npoints=int(self.npoints)

        #Calculate corner point coordinates
        x0, x1 = self.x-self.width*0.5, self.x+self.width*0.5
        y0, y1 = self.y-self.height*0.5, self.y+self.height*0.5

        #Calculate perimeter length
        perimeter = 2.0*self.width + 2.0*self.height

        #Calculate distance between points
        dp = float(perimeter)/npoints

        #Calculate horizontal and vertical points per side

        nHpoints = self.width/dp
        nVpoints = self.height/dp

        #Start drawing at <x0,y0>
        x = x0
        y = y0

        for i in range(npoints):

            if i < int(nVpoints):
                self.add_point(Point(x,y))
                y += dp


            elif i == int(nVpoints):
                self.add_point(Point(x,y))
                remainder = y1 - y
                y = y1
                x = x0
                x += remainder


            elif i < int(nVpoints + nHpoints):
                self.add_point(Point(x,y))
                x += dp


            elif i == int(nVpoints + nHpoints):
                self.add_point(Point(x,y))
                remainder = x1 - x
                x=x1
                y = y1 - remainder


            elif i < int(2 * nVpoints + nHpoints):
                self.add_point(Point(x,y))
                y -= dp


            elif i == int(2 * nVpoints + nHpoints):
                self.add_point(Point(x,y))
                remainder = y - y0
                y = y0
                x = x1
                x -= remainder


            else:
                self.add_point(Point(x,y))
                x -= dp

class Line(Shape):
    """
    A line between two Point objects, containing npoints number of points
    """
    def __init__(self, Point0, Point1, npoints):
        self.x0 = Point0.get_x()
        self.y0 = Point0.get_y()
        self.x1 = Point1.get_x()
        self.y1 = Point1.get_y()
        self.length = math.sqrt((self.x1-self.x0)**2+(self.y1-self.y0)**2)
        Shape.__init__(self, Point((self.x1-self.x0)/2.0,(self.y1-self.y0)/2.0)
                       , npoints, 'line')
        self._coordgen()

    def _coordgen(self):
        """
        Adds npoints equally spaced points along the line.

        """

        #First we add the endpoints
        #self.add_point(Point(self.x0, self.y0))
        #self.add_point(Point(self.x1, self.y1))

        dx = float(self.x1-self.x0)/(self.npoints-1)
        dy = float(self.y1-self.y0)/(self.npoints-1)
        x = self.x0
        y = self.y0
        for i in range(self.npoints):
            x = self.x0 + i * dx
            y = self.y0 + i * dy
            self.add_point(Point(x, y))
