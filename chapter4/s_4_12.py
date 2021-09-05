from itertools import chain

if __name__ == '__main__':
    print("-- 不同集合上元素的迭代 --")
    print()

    a = range(0, 5)
    b = range(5, 10)
    for x in chain(a, b):
        print(x, end="\t")
