def frange(start, stop, inc):
    x = start
    while x < stop:
        yield x
        x += inc


if __name__ == '__main__':
    print("-- 使用生成器创建新的迭代模式 --")
    print()

    print("浮点数迭代器")
    for f in frange(0, 4, 0.6):
        print("{:.1f}".format(f))
    print(list(frange(0,1,0.125)))
    print(list(frange(0,4,0.6)))
