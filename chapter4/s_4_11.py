from itertools import zip_longest

if __name__ == '__main__':
    print("-- 同时迭代多个序列 --")
    print()

    print("-- 使用 zip，会以最短的一个序列（迭代器）为准返回元素 --")
    xpts = range(0, 6)
    ypts = range(5, 10)
    for x, y in zip(xpts, ypts):
        print(x, y)

    print("-- 使用 zip_longest 以最长的序列为准，可以指定缺省值 --")
    for x, y in zip_longest(range(0, 6), range(5, 10), fillvalue=0):
        print(x, y)
