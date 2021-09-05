import itertools

if __name__ == '__main__':
    print("-- 排列组合的迭代 --")
    print()

    items = ['a', 'b', 'c']
    print("-- permutations 全排列 --")
    for p in itertools.permutations(items):
        print(p)
    print("指定长度的排列")
    for p in itertools.permutations(items, 2):
        print(p)

    print()

    print("-- combinations 组合 --")
    for i in range(1, 4):
        print("组合长度 {}".format(i))
        for c in itertools.combinations(items, i):
            print(c)
