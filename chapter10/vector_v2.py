# encoding=utf-8
from array import array
import reprlib
import math
from numbers import Integral

class Vector:
    typecode = 'd'

    def __init__(self, compoents):
        self.__compoents = array(self.typecode, compoents)

    def __iter__(self):
        return iter(self.__compoents)

    def __repr__(self):
        components = reprlib.repr(self.__compoents)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self.__compoents))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self.__compoents)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self.__compoents)

    def __getitem__(self, item):
        if isinstance(item, Integral):
            return self.__compoents[item]
        elif isinstance(item, slice):
            return (type(self))(self.__compoents[item])
        else:
            raise TypeError

    @classmethod
    def from_bytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector(range(10))
    print(repr(v1))
    print(str(v1))
    for x in v1:
        print(x, end=' ')
    print('')
    octets = bytes(v1)
    print(octets)
    v1_clone = Vector.from_bytes(octets)
    print(v1_clone)
    print(repr(v1[1:5])) #Vector([1.0, 2.0, 3.0, 4.0])
