# encoding = utf-8
# encoding=utf-8
from array import array
import math

# immutable and hashable
# 并不能真正的实现私有和不可变，只是防止无意间的访问
class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):  # 对构造方法的准确描述
        classname = type(self).__name__
        return '{0}({1}, {2})'.format(classname, self.x, self.y)

    def __str__(self):  # 对对象本身内容的描述
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __mul__(self, other):
        num = float(other)
        return Vector2d(self.x * num, self.y * num)

    def __rmul__(self, other):
        num = float(other)
        return Vector2d(self.x * num, self.y * num)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        v2 = Vector2d(*other)
        return Vector2d(self.x + v2.x, self.y + v2.y)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1)
    print(repr(v1))
    print(str(v1))
    x, y = v1
    print(x, y)
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    octets = bytes(v1)
    print(octets)
    print(Vector2d.frombytes(octets))
    v2 = [4, 5]
    v3 = Vector2d(6, 7)
    print(v1 + v2)
    print(v1 + v3)
    print(v1 * 2)
    print(2 * v1)
    #read only test
    try:
        v1.x = 1
    except AttributeError:
        print("Read only!")

    print(v1)
    # hash test
    v1 = Vector2d(3,4)
    v2 = Vector2d(3.1, 4.2)
    print(hash(v1), hash(v2))


