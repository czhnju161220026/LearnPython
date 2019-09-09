# encoding=utf-8
import numpy as np


def output(nd):
    print('_' * 80)
    print(nd, nd.shape, type(nd))


if __name__ == '__main__':
    nd = np.array(range(20)).reshape((4, 5))
    output(nd)
    output(nd[1:3])
    output(nd[1:, 2:])
    output(nd[[0, 3]])
