from point import Point
from shape import Shape


class Ellipse(Shape): # Inherits from the shape class
    """Defines an ellipse class. """

    def __init__(self, num_sides = 0, centre_point = Point(0,0,0),
    x_radius = 0, y_radius = 0):
        Shape.__init__(self, num_sides, centre_point) # constructor for base class
        self.x_radius = x_radius
        self.y_radius = y_radius

    def __str__(self):
        s = Shape.__str__(self) +','+'\n'
        s = s + 'x_radius = ' + str(self.x_radius)+','+'\t'
        s = s + 'y_radius = ' + str(self.y_radius)
        return s

