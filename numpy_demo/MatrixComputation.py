# encoding=utf-8
import numpy as np

def output(nd):
    print('_' * 80)
    print(nd, nd.shape, type(nd))

if __name__ == '__main__':
    nd = np.arange(1,10).reshape((3,3))
    output(nd)
    output(nd.transpose())
    # 矩阵乘法
    nd2 = np.diag([1,2,3])
    output(nd2.dot(nd))

    # 求矩阵的迹
    output(nd.trace())

    #行列式
    output(np.linalg.det(nd))

    # 求逆
    output(np.linalg.inv(nd2))

    # 特征值与特征向量
    values, vectors = np.linalg.eig(nd)
    print(values)
    print(vectors)

    #




