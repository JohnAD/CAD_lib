###################################
#
#    Point
#
###################################
class Point(object):
    '''
       A point.
    '''
    def __init__(self, x=0.0, y=0.0, z=None):
        if hasattr(x, 'x'):  # is this an objext containing x,y,z objects? If so, then transfer those.
            tx = x.x
            ty = y
            tz = z
            if hasattr(x, 'y'):
                ty = x.y
            if hasattr(x, 'z'):
                tz = x.z    
            self._assign(tx, ty, tz)
        else:
            self._assign(x, y, z)
        self.area = 0.0  # by definition
        self.bounds = (0.0, 0.0, 0.0, 0.0) # by defition
        self.length = 0.0  # by definition
        self.geom_type = "Point"
        return

    #
    # CLASS SPECIAL METHODS
    #

    def __repr__(self):
        if self.z is None:
            result = "<CAD_lib.geometry.Point ({}, {})>".format(self.x, self.y)
        else:
            result = "<CAD_lib.geometry.Point ({}, {}, {})>".format(self.x, self.y, self.z)
        return result

    def __str__(self):
        if self.z is None:
            result = "Point ({}, {})".format(self.x, self.y)
        else:
            result = "Point ({}, {}, {})".format(self.x, self.y, self.z)
        return result

    #
    # INTERNAL METHODS
    #

    def _assign(self, x, y, z):
        if type(x) is tuple or type(x) is list:
            if len(x)==3:
                (x,y,z) = x
            elif len(x)==2:
                (x,y) = x
            elif len(x)==1:
                x = x[0]
        self.x = float(x)
        self.y = float(y)
        if z is None:
            self.z = None
            self.coords = [(x, y)]
        else:
            self.z = float(z)
            self.coords = [(x, y, z)]
        return


    #
    # GENERAL OBJECT ROUTINES:
    #
    # def distance(self, other):
    # def representative_point(self):

###################################
#
#   Line
#
###################################

class Line(object):
    '''
       A Line is an ordered list of strictly two Points
    '''
    def __init__(self, a, b):
        self.area = 0
        self.length = 0.0 #TBD
        self.bounds = None #TBD
        self.a = Point(a)
        self.b = Point(b)
        self._reparse()
        return

    #
    # CLASS SPECIAL METHODS
    #

    def __repr__(self):
        result = "<CAD_lib.geometry.Line {}>".format(str(self.coord))
        return result

    def __str__(self):
        result = "Line {}".format(str(self.coord))
        return result

    #
    # INTERNAL METHODS
    #

    def _reparse(self):
        self._ls = LineString([self.a, self.b])
        self.coord = self._ls.coord
        return
    #
    # GENERAL OBJECT ROUTINES:
    #
    # def distance(self, other):
    # def representative_point(self):

    

    
###################################
#
#    LineString
#
###################################
class LineString(object):
    '''
       A LineString is an ordered list of Points
    '''
    def __init__(self, coordinates):
        self.area = 0
        self.length = 0.0 #TBD
        self.bounds = None #TBD
        if hasattr(coordinates, "coord"):
            self._parse_coordinates(coordinates.coord)
        else:
            self._parse_coordinates(coordinates)
        return

    #
    # CLASS SPECIAL METHODS
    #

    def __repr__(self):
        result = "<CAD_lib.geometry.LineString with {} Points>".format(len(self._true_coord))
        return result

    def __str__(self):
        result = "LineString {}".format(str(self.coord))
        return result

    #
    # INTERNAL METHODS
    #

    def _parse_coordinates(self, coordinates):
        self._true_coord = []
        self.coord = []
        for p in coordinates:
            true_point = Point(p)
            self._true_coord.append(true_point)
            if true_point.z is None:
                self.coord.append((true_point.x, true_point.y))
            else:
                self.coord.append((true_point.x, true_point.y, true_point.z))
        return
    #
    # GENERAL OBJECT ROUTINES:
    #
    # def distance(self, other):
    # def representative_point(self):

    