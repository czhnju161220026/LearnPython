# encoding=utf-8
from array import array
import reprlib
import math
from numbers import Integral
from functools import reduce
from operator import xor


# 第四版 散列与快速等值
class Vector:
    typecode = 'd'

    def __init__(self, compoents):
        self.__compoents = array(self.typecode, compoents)

    shortcut_names='xyzt'
    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut_names.find(item)
            if 0 <= pos < len(self.__compoents):
                return self.__compoents[pos]
        raise AttributeError

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_names:
                error = 'readonly attribute {attr_name:s}'
            elif key.islower():
                error = 'can\'t set attribute \'a\' to \'z\' in {cls_name:s}'
            else:
                error =' '
            if error:
                msg = error.format(attr_name=key, cls_name=cls)
                raise AttributeError(msg)
        super().__setattr__(key, value)


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
        #return tuple(self) == tuple(other)
        if len(self) != len(other):
            return False
        for a,b in zip(self, other):
            if a != b:
                return False
        return True

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

    def __hash__(self):
        #hashes = (hash(x) for x in self.__compoents)
        hashes = map(hash, self.__compoents)
        return reduce(xor, hashes)


    @classmethod
    def from_bytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector([1,2.5,3.4,1.4,5,6])
    print(repr(v1))
    print(str(v1))
    for x in v1:
        print(x, end=' ')
    print('')
    octets = bytes(v1)
    print(octets)
    v1_clone = Vector.from_bytes(octets)
    print(v1_clone==v1)
    print(repr(v1[1:5]))  # Vector([1.0, 2.0, 3.0, 4.0])
    print(v1.x,v1.y,v1.z)
    print(hash(v1), hash(v1_clone))
