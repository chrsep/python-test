from sys import exc_info
from math import hypot


class Point(object):

    def __init__(self, a, *b):
        self.P = self.ConvertTo(a, *b)

    def __repr__(self):
        return str(self.P)

    def __getitem__(self, i):
        return self.P[i]

    def __eq__(self, *a):
        x = Point(*a)
        return self.P == x.P

    def __ne__(self, *a):
        x = Point(*a)
        return not self == x

    def __lt__(self, *a):
        x = Point(*a)
        return (self.P[0] < x.P[0]) and (self.P[1] < x.P[1])

    def __le__(self, *a):
        x = Point(*a)
        return (self.P[0] <= x.P[0]) and (self.P[1] <= x.P[1])

    def __gt__(self, *a):
        x = Point(*a)
        return (self.P[0] > x.P[0]) and (self.P[1] > x.P[1])

    def __ge__(self, *a):
        x = Point(*a)
        return (self.P[0] >= x.P[0]) and (self.P[1] >= x.P[1])

    def __add__(self, *a):
        x = Point(*a)
        x.P = [x.P[0] + self.P[0], x.P[1] + self.P[1]]
        return x

    def __iadd__(self, *a):
        x = Point(*a)
        self = self + x
        return self

    def __sub__(self, *a):
        x = Point(*a)
        x.P = [self.P[0] - x.P[0], self.P[1] - x.P[1]]
        return x

    def __isub__(self, *a):
        x = Point(*a)
        self = self - x
        return self

    def __mul__(self, *a):
        x = Point(0, 0)
        y = self.GetOperand(*a)
        x.P = (self.P[0] * y, self.P[1] * y)
        return x

    def __imul__(self, *a):
        self.P = self.__mul__(*a).P
        return self

    def __truediv__(self, *a):
        x = Point(0, 0)
        y = self.GetOperand(*a)
        x.P = (self.P[0] / y, self.P[1] / y)
        return x

    def __itruediv__(self, *a):
        self.P = self.__truediv__(*a).P
        return self

    def length(self):
        return hypot(self.P[0], self.P[1])

    def copy(self):
        x = Point(self.P)
        return x

    def x(self):
        return self.P[0]

    def y(self):
        return self.P[1]

    def GetOperand(self, *a):
        if (len(a) == 1):
            x = self.Collapse(*a)
            if (type(x) in (int, float)):
                return x
        raise (SyntaxError("\n  Syntax Error:" + str(a) + " is not a number.\n"))

    def Collapse(self, a):
        while (1):
            if (type(a) == Point):
                a = a.P
            elif (type(a) in (list, tuple)) and (len(a) == 1):
                a = a[0]
            else:
                break
        return a

    def ConvertTo(self, a, *b):
        a = self.Collapse(a)
        try:
            if b == ():
                if (type(a) == complex):
                    return (a.real, a.imag)
                elif (len(a) == 2):
                    if (type(a[0]) in (float, int)) and (type(a[1]) in (float, int)):
                        return (a[0], a[1])
                raise (SyntaxError("\n  Syntax Error:" + str(a) + " cannot convert to coordinates.\n"))
            b = self.Collapse(b)
            if (type(a) in (float, int)) and (type(b) in (float, int)):
                return (a, b)
        except:
            pass
        raise (SyntaxError("\n  Syntax Error:" + str(a) + "," + str(b) + " cannot convert to coordinates.\n"))