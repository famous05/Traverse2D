from point import Point
from shape import Shape


class Rectangle(Shape):
    """Defines a rectangle class. """

    def __init__(self, num_sides=0, centre_point=Point(0, 0, 0),
                 bottom_left_point=Point(0, 0, 0), top_right_point=Point(0, 0, 0)):
        Shape.__init__(self, num_sides, centre_point) # constructor for base class
        self.bottom_left_point = bottom_left_point
        self.top_right_point = top_right_point
        self.width = top_right_point.x - bottom_left_point.x
        self.height = top_right_point.y - bottom_left_point.y 


    def __str__(self):
        s = Shape.__str__(self) +','+'\n'
        s = s + 'Bottom left point = ' + self.bottom_left_point.__str__()+','+'\t'
        s = s + 'Top right point = ' + self.top_right_point.__str__()
        return s

    def set_bounds(self, bottom_left_point = Point(0,0,0), top_right_point = Point(0,0,0)):
        self.bottom_left_point = bottom_left_point
        self.top_right_point = top_right_point
        self.width = top_right_point.x - bottom_left_point.x
        self.height = top_right_point.y - bottom_left_point.y 


    def set_width_height(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.bottom_left_point.set_xyz(0,0,0)
        self.top_right_point.set_xyz(width,height,0)

    #def draw_points()
    #def draw_outline()
