from Point import *


class Points():
    def __init__(self, *a):
        self.Pts = []
        if (len(a) == 0):  # TODO: THIS MIGHT NOT BE THE RIGHT FIX !!!!!!! BE CAREFUL (turn a to len(a))
            return 0;

        if (callable(a[0])):
            try:
                if not all(isinstance(item, int) for item in a[1:]) or len(a) == 1:
                    raise SyntaxError
                for x in range(*a[1:3]):
                    y = a[0](x)
                    self.Pts.append(Point(x, y))
            except:
                print("The point describe for the range were incorrect !!!!")
        else:
            self.Pts = self.createPointList(a)

    def createPointList(self, *a):
        x = []
        try:
            x.append(Point(a))
            return x
        except:
            for ps in a:
                for item in ps:
                    x += self.createPointList(item)
            return x

    def __repr__(self):
        a = ""
        for x in self.Pts:
            a += str(x)
        return '<' + a + '>'

    def length(self):
        length = float(0)
        for x in range(1, len(self)):
            length += (self[x - 1] - self[x]).length()
        return length  # TODO: THIS IS NOT RIGHT !!!!!!!!! REMEMBER TO FIX

    def __len__(self):
        return len(self.Pts)

    def __index(self, *a):
        y = self.createPointList(*a) 
        start_point = y[0]
        start_idx = -1
        arr_len = len(self.Pts)
        for idx in range(len(self)):
            if self.Pts[idx] == start_point:
                start_idx = idx
                break

        if start_idx == -1:
            return -1, 0

        relative_start = start_idx + arr_len
        relative_end = len(y) + relative_start
        idx = 0
        for relative_idx in range(relative_start, relative_end):
            subject = self.Pts[relative_idx % arr_len]
            if subject != y[idx]:
                return -1, 0
            idx += 1

        return start_idx, len(y)

    def index(self, *a):
        return self.__index(a)[0]

    def __contains__(self, *a):
        return self.__index(a)[0] != -1

    def __eq__(self, a):
        try:
            if len(self) != len(a):
                return False
            for x in range(1, len(self)):
                self_difference = self[x - 1] - self[x]
                a_difference = a[x - 1] - a[x]
                if(self_difference != a_difference):
                    return False
            return True
        except:
            return False

    def __add__(self, *a):
        y = self.createPointList(*a) 
        return Points(self.Pts + y)

    def __iadd__(self, *a):
        y = self.createPointList(*a) 
        self.Pts = self.Pts + y
        return self

    def __sub__(self, *a): # TODO: This is not finished
        idx, length = self.__index(a)
        if idx == -1:
            raise IndexError
        new_point = Points(self)
        for x in a[0]:
            new_point.Ptr.remove(x)
        return new_point


    def __isub__(self, *a):
        ...

    def __getitem__(self, x):
        return self.Pts[x]

    def __setitem__(self, y, x):
        self.Pts[y] = Point(x)

    def __delitem__(self, y):
        del self.Pts[y]


if __name__ == "__main__":
    def test(lhs, op, rhs, res, expected):
        print("Try: ", lhs, op, rhs, " = ", res, end="")
        if res == expected:
            print("(correct)")
        else:
            print("(INCORRECT!)")