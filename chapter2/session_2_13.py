if __name__ == '__main__':
    print("-- 字符串对齐 ljust/rjust/center --")
    str = "hello world"
    print("ljust")
    print(str.ljust(20, '*'))
    print("rjust")
    print(str.rjust(20, '*'))
    print("center")
    print(str.center(20, '*'))
    print("\n")

    print("-- 使用 format 格式化 --")
    print("ljust")
    print(format(str, '*>20'))
    print("rjust")
    print(format(str, '*<20'))
    print("center")
    print(format(str, '*^20'))
