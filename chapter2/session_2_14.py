if __name__ == '__main__':
    print("-- 合并拼接字符串 --")
    print()

    print("-- 使用 join 拼接序列、iterable --")
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print("序列 ： {}".format(parts))
    print("空格拼接后 ： [{}]".format(' '.join(parts)))
