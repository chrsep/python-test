from Point import *
from Points import *
from math import acos, pi


class Almost():
    def __init__(self, a):
        ...

    def __add__(self, a):
        ...

    def __eq__(self, a):
        ...

    def __ne__(self, a):
        ...


class Shape():
    ...


class Angle():
    def __init__(self, a):
        p1 = a[1] - a[0]
        p2 = a[2] - a[1]
        inner_product = p1.x() * p2.x() + p1.y() * p2.y()
        self.angle = Almost(180 * acos(inner_product / (p1.length() * p2.length())) / pi)


class Polygon(Points, Shape):
    def length(self):
        ...


class Triangle(Polygon):
    def __init__(self, *a):
        ...


class Quadrilateral(Polygon):
    def __init__(self, *a):
        ...


class Trapezoid(Quadrilateral):
    def __init__(self, *a):
        ...


class Parallelogram(Trapezoid):
    def __init__(self, *a):
        ...


class Rhombus(Parallelogram):
    def __init__(self, *a):
        ...


class Rectangle(Parallelogram):
    def __init__(self, *a):
        ...


class Square(Rhombus, Rectangle):
    def __init__(self, *a):
        ...


class Circle(Shape, Point):
    def __init__(self, *a):
        ...

    def __repr__(self):
        ...

    def length(self):
        ...
