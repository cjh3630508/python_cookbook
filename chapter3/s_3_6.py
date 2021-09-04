if __name__ == '__main__':
    print("-- 负数的数学运算 --")
    print("-- numpy 模块支持复数 --")
    print("-- cmath 模块支持复数计算 --")
    print()

    print("-- 使用 complex --")
    num = complex(3, 4)
    print("num={}".format(num))
    print()

    print("-- 使用 j 表示负数 --")
    num = 3 + 4j
    print("num={}".format(num))
    print()

    print("{} 的实部 = {}".format(num, num.real))
    print("{} 的虚部 = {}".format(num, num.imag))
    print("{} 的共轭复数 = {}".format(num, num.conjugate()))
    print()

    print("-- 计算 --")
    num1 = num
    num2 = 2 - 3j
    print("{}+{}={}".format(num1, num2, num1 + num2))
    print("{}-{}={}".format(num1, num2, num1 - num2))
    print("{}*{}={}".format(num1, num2, num1 * num2))
    print("{}/{}={}".format(num1, num2, num1 / num2))

