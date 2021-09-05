import itertools

if __name__ == '__main__':
    print("-- 跳过可迭代对象的开始部分 --")
    print()

    for x in itertools.dropwhile(lambda x: x < 5, range(0, 10)):
        print(x, end='\t')
