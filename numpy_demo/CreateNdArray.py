import numpy as np


def output(nd):
    print('_' * 80)
    print(nd, nd.shape, type(nd))


if __name__ == '__main__':
    nd1 = np.array([1, 2, 3, 4, 5, 6])
    output(nd1)
    nd2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    output(nd2)
    np.random.shuffle(nd2)
    output(nd2)
    nd3 = np.random.random((4, 2))
    output(nd3)
    # 利用arrange创建
    nd4 = np.arange(1,10,0.5)
    output(nd4)

    # 创建特殊的ndarray
    output(np.zeros((1, 3)))
    output(np.ones((1, 4)))
    output(np.eye(5))  # 单位矩阵
    output(np.diag([1, 2, 3, 4]))  # 对角矩阵

    # 改变数组的形状
    nd1_2 = nd1.reshape((-1, 2))
    output(nd1_2)

    # 存取
    nd9 = np.random.random((5, 5))
    np.savetxt(fname='nd9.txt', X=nd9)
    nd10 = np.loadtxt('nd9.txt')
    output(nd10)
