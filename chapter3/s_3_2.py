from decimal import Decimal

if __name__ == '__main__':
    print("-- 执行精确的浮点运算 --")
    print()

    print("-- 普通运算 --")
    a = 4.2
    b = 2.1
    c = a + b
    print("{}+{}={}".format(a, b, c))
    print()

    print("-- 使用 decimal 模块 --")
    a = Decimal('4.2')
    b = Decimal('2.1')
    c = a + b
    print("{}+{}={}".format(a, b, c))
    print(c == Decimal('6.3'))
