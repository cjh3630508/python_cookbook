def round_test(num, precision):
    print("{} 保留 {} 位小数 ： {}".format(num, precision, round(num, precision)))


def foramt_test(num, precision):
    print("{} 保留 {} 位小数 ： {}".format(num, precision, format(num, '0.' + str(precision) + 'f')))


def str_format_test(num, precision):
    print(("{} 保留 {} 位小数 ： {:0." + str(precision) + "f}").format(num, precision, num))


if __name__ == '__main__':
    print("-- 数字的四舍五入 --")
    print()

    print("-- round 进行简单的四舍五入，在边界中间的（5)，round 返回距离最近的偶数 --")
    round_test(1.23, 1)
    round_test(1.25, 1)
    round_test(1.27, 1)
    round_test(1.25361, 3)
    print()

    print("-- format(num,precision) 格式化输出，会进行普通的四舍五入 --")
    x = 1.23456
    foramt_test(x, 1)
    foramt_test(x, 2)
    foramt_test(x, 3)
    print()

    print("-- 字符串.format 格式化输出 --")
    str_format_test(x, 1)
    str_format_test(x, 2)
    str_format_test(x, 3)
