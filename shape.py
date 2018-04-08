from point import Point


class Shape(object):

    """Defines a shape class. """

    def __init__(self, num_sides = 0, centre_point = Point(0,0,0)):
        self.num_sides = num_sides
        self.centre_point = centre_point
        self.points = []

    def __str__(self):
        s = 'Num sides = ' +str(self.num_sides)+',' +('\t') +'Centre point = '
        s = s + self.centre_point.__str__()
        return s

        
    def set_num_of_sides(self, num_sides):
        self.num_sides = num_sides

    def print_points(self):
        for i, point in enumerate(self.points):
            print (point)


    #def draw_points()
    #def draw_outline()
