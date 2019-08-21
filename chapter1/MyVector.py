from math import hypot


class MyVector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # like toString in Java
    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __add__(self, other):
        return MyVector(x=self.x + other.x, y=self.y + other.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        #return bool(abs(self))
        return bool(self.x or self.y)

    # vector * scalar
    def __mul__(self, scalar):
        return MyVector(x=self.x * scalar, y=self.y * scalar)

    # scalar * vector
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

if __name__ == '__main__':
    v = MyVector(x=3, y=4)
    print(v)
    print(str(v))
    print(abs(v))
    print(v*5)
    print(5*v)
    v2 = MyVector(x=1)
    print(v + v2)
    print(bool(v))
