#!/usr/bin/python
from point import Point
from shape import Shape
from rectangle import Rectangle
from ellipse import Ellipse

def main():
    
    p = Point(1,2,3)
    p.print_point()
    print (p)

    s = Shape(5,p)
    print (s)
    s.print_points()

    r = Rectangle()
    p2 = Point(6,6,6)
    r.centre_point = p2
    r.set_bounds(p)
    print (r)
    print (p2)

    r.points.append(p)
    r.points.append(p2)

    r.print_points()

    e = Ellipse()
    print (e)


if __name__ == '__main__':
    main()
