def print_format(info, str):
    print(info)
    print("[{}]".format(str))


if __name__ == '__main__':
    print("-- 数字的格式化输出 --")
    print()

    print("-- 使用内置的 format() 函数，字符串格式 {:格式化信息} --")
    print("-- 一般格式 '[<>^]?width[,]?(.digits)?' --")
    x = 1234.56789
    print_format("普通输出", format(x, '0.2f'))
    print_format("右对齐", format(x, '>10.1f'))
    print_format("左对齐", format(x, '<10.1f'))
    print_format("居中对齐", format(x, '^10.1f'))
    print_format("千位数分割", format(x, '10,.1f'))
