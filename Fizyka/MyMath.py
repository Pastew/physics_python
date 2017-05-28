from numbers import Number
from math import sqrt


class Wektor:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def dlugosc(self):
        return sqrt(self.x * self.x +
                    self.y * self.y +
                    self.z * self.z)

    def normuj(self):
        dlugosc = self.dlugosc()
        self.x /= dlugosc
        self.y /= dlugosc
        self.z /= dlugosc
        return self

    def __add__(self, other):
        return Wektor(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other):
        return Wektor(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def __mul__(self, other):
        result = Wektor()
        if other.__class__ is Wektor:
            return self.x * other.x + self.y * other.y + self.z * other.z

        if isinstance(other, Number):
            return Wektor(self.x * other,
                          self.y * other,
                          self.z * other)

        print "I don't know that type: " + str(type(other))
        print "Class: " + str(other.__class__)  # TODO: remove this
        return result

    def __div__(self, other):
        if type(other) is float:
            return Wektor(self.x / other,
                          self.y / other,
                          self.z / other)

        if isinstance(other, Number):
            return Wektor(self.x * other,
                          self.y * other,
                          self.z * other)

        print "I don't know that type: " + str(type(other))
        print "Class: " + str(other.__class__)  # TODO: remove this

    def __str__(self):
        return "[%s, %s, %s]" % (self.x, self.y, self.z)

    def div(self, some_float):
        return Wektor(self.x / some_float,
                      self.y / some_float,
                      self.z / some_float)

    def xyz(self):
        return [self.x, self.y, self.z]


class Wersor:
    def __init__(self, x=0, y=0, z=0):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)


class WersoryKierunkowe:

    wersory_kierunkowe_2D = [
    Wersor(0, 1, 0), Wersor(1, 1, 0),
    Wersor(1, 0, 0), Wersor(1, -1, 0),
    Wersor(0, -1, 0), Wersor(-1, -1, 0),
    Wersor(-1, 0, 0), Wersor(-1, 1, 0)
]


class Kolor:
    def __init__(self, r=1.0, g=1.0, b=1.0, a=1.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def rgb(self):
        return [self.r, self.g, self.b]
