if __name__ == '__main__':
    print("-- 序列上索引值迭代 --")
    print()

    print("正常索引")
    for idx, val in enumerate(range(0, 5)):
        print(idx, val)

    print("指定起始索引编号（不是跳过开始部分）")
    for idx, val in enumerate(range(0, 5),1):
        print(idx, val)
