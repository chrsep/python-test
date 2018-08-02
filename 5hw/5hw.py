
from sys import exc_info

# Explanations and tests redacted
class Point(object):
 
    def __init__(self, a, *b):
        self.P = self.ConvertTo(a, *b)

    def __str__(self):
        return "({}, {})".format(self.P[0], self.P[1])  # TODO: This might suppose to return a value

    def __eq__(self, *a):
        return self.x() == a[0].x() and self.y() == a[0].y()

    def __ne__(self, *a):
        return not self == a

    def __lt__(self, *a):
        return self.x() < a[0].x() and self.y() < a[0].y()

    def __le__(self, *a):
        return self.x() <= a[0].x() and self.y() <= a[0].y()

    def __gt__(self, *a):
        return not self < a

    def __ge__(self, *a):
        return not self <= a

    def __add__(self, *a):
        new_point = Point(*a)
        return Point(self.x() + new_point.x(), self.y() + new_point.y())

    def __sub__(self, *a):
        new_point = Point(*a)
        return Point(self.x() - new_point.x(), self.y() - new_point.y())

    def __mul__(self, *a): # TODO: this might be wrong
        new_point = Point(0, 0)
        operand= self.GetOperand(*a)
        new_point.P = (self.x() * operand, self.y() * operand)
        return new_point

    def __truediv__(self, *a): # TODO: this might be wrong
        new_point = Point(0, 0)
        operand= self.GetOperand(*a)
        new_point.P = (self.x() / operand, self.y() / operand)
        return new_point

    def __iadd__(self, *a):# TODO: this might be wrong
        return self + a

    def __isub__(self, *a):# TODO: this might be wrong
        return self - a

    def __imul__(self, *a):# TODO: this might be wrong
        return self * a

    def __itruediv__(self, *a):# TODO: this might be wrong
        return self / a

    def copy(self):
        return Point(self.x(), self.y())

    def x(self):
        return self.P[0]

    def y(self):
        return self.P[1]

    def GetOperand(self, *a):
        if len(a) == 1:  
            reduced_a = self.Collapse(*a) 
            if isinstance(reduced_a, int): 
                return reduced_a 
        raise SyntaxError("Non Scalar was given")

    def Collapse(self, a):
        if isinstance(a, int) or isinstance(a, Point):
            return a
        if isinstance(a, complex):
            return a.real, a.imag
        isfinal = isinstance(a[0], int) or isinstance(a[0], Point)
        return a if isfinal and len(a) > 1 else self.Collapse(a[0])

    def ConvertTo(self, a, *b):
        no_b = len(b) == 0
        a2 = self.Collapse(a)
        b2 = None if no_b else self.Collapse(b)
        if no_b:
            return (a2.x(), a2.y()) if isinstance(a2, Point) else (a2[0], a2[1])
        elif isinstance(a2, int) and isinstance(b2, int):
            return a2, b2
        raise SyntaxError("cannot convert to coordinates")
