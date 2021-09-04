import numpy as np

if __name__ == '__main__':
    print("-- 矩阵与线性代数运算 numpy --")
    print()

    print("-- 矩阵基本运算 --")
    m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print("矩阵 m={}".format(m))
    print()
    print("m 的转置={}".format(m.T))
    print()
    print("m 的逆={}".format(m.I))
    v = np.matrix([[2], [3], [4]])
    print("v={}".format(v))
    print("m*v={}".format(m * v))
