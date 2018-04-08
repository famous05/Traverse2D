class Point(object):

    """Defines a 3-dimensional point (X, Y, Z)"""

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '(%s, %s, %s)' % (self.x, self.y, self.z)

    def set_xyz(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print_point(self):
        """Prints the point to screen
        """
        print('%s, %s, %s' % (self.x, self.y, self.z))
