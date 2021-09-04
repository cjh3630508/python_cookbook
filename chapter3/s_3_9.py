import numpy as np

if __name__ == '__main__':
    print("-- 大型数组运算 --")
    print("-- numpy 计算比 math 模块更快 --")
    print()

    print("-- 普通数组操作，结果不是数学运算 --")
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print("x={}".format(x))
    print("y={}".format(y))
    print("x*2={}".format(x * 2))
    print("x+y={}".format(x + y))
    print()

    print("-- 使用 numpy --")
    ax = np.array(x)
    ay = np.array(y)
    print("ax={}".format(ax))
    print("ay={}".format(ay))
    print("ax*2={}".format(ax * 2))
    print("ax+ay={}".format(ax + ay))
    print("ax*ay={}".format(ax * ay))
    print("ax/ay={}".format(ax / ay))
    print()

    print("-- numpy 扩展 python 列表的索引功能 --")
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print("a={}".format(a))
    print("a[1]={}".format(a[1]))
    print("a[:1]={}".format(a[:, 1]))
    print("a[1:3,1:3]={}".format(a[1:3, 1:3]))
    row = [1, 2, 3, 4]
    print("a+{}={}".format(row, a + row))
