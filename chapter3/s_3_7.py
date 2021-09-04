import math

if __name__ == '__main__':
    print("-- 无穷大与 NaN --")
    print()

    print("-- 创建无穷大与 NaN --")
    a = float('inf')
    b = float('-inf')
    c = float('nan')
    print("a={}".format(a))
    print("b={}".format(b))
    print("c={}".format(c))
    print("a is inf : {}".format(math.isinf(a)))
    print("b is inf : {}".format(math.isinf(b)))
    print("c is nan : {}".format(math.isinf(c)))
