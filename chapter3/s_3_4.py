if __name__ == '__main__':
    print("-- 二八十六进制整数 --")
    print()

    x = 1234
    print("x={}".format(x))
    print()

    print("-- 带前缀输出 --")
    print("bin(x)={}".format(bin(x)))
    print("oct(x)={}".format(oct(x)))
    print("hex(x)={}".format(hex(x)))
    print()

    print("-- 不带前缀输出 --")
    print("bin(x)={}".format(format(x, 'b')))
    print("oct(x)={}".format(format(x, 'o')))
    print("hex(x)={}".format(format(x, 'x')))
    print()

    x = -1234
    print("-- 带符号输出负数 --")
    print("bin(x)={}".format(format(x, 'b')))
    print("oct(x)={}".format(format(x, 'o')))
    print("hex(x)={}".format(format(x, 'x')))
    print()

    print("-- 不带符号输出负数，指定最大长度，比如 32 --")
    print("bin(x)={}".format(format(2 ** 32 + x, 'b')))
    print("oct(x)={}".format(format(2 ** 32 + x, 'o')))
    print("hex(x)={}".format(format(2 ** 32 + x, 'x')))
    print()

    print("-- n 进制转 10 进制 int(num,--")
    print('int("4d2",16)={}'.format(int('4d2', 16)))
    print('int("10011010010",2)={}'.format(int('10011010010', 2)))
