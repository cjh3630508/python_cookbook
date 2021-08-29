class SafeSub(dict):
    # 提供找不到 key 的默认返回值
    def __missing__(self, key):
        return '{' + key + '}'


if __name__ == '__main__':
    print("-- 字符串中插入变量 --")
    print()

    print("-- 普通 format 替换 --")
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))
    print()

    print("-- format_map() 和 vars() 替换 --")
    name = 'Guido'
    n = 37
    print(s.format_map(vars()))
    print()

    print("-- 变量缺失处理 __missiong__() 方法 --")
    print("-- 定义一个含有 __missing__() 方法的字典对象 --")
    del n
    print(s.format_map(SafeSub(vars())))
