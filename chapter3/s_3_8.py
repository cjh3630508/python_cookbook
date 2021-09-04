from fractions import Fraction

if __name__ == '__main__':
    print("-- 分数运算 --")
    print()

    print("-- 使用 fractions 模块 --")
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print("a={}".format(a))
    print("b={}".format(b))
    print("{}+{}={}".format(a, b, a + b))
    print("{}-{}={}".format(a, b, a - b))
    print("{}*{}={}".format(a, b, a * b))
    print("{}/{}={}".format(a, b, a / b))
    print()

    print("a={},分子：{}，分母：{}".format(a, a.numerator, a.denominator))
    print("a={},转为小数={}".format(a, float(a)))
    c = a * b
    print("最接近 {} 且分母不大于 {} 的数为 {}".format(c, 10, c.limit_denominator(10)))
