import os

if __name__ == '__main__':
    print("-- 字符串开头或结尾匹配 --")
    print("startwith,endwith")
    filename = "abc.txt"
    print(filename.startswith("abc"))
    print(filename.startswith("aaa"))
    print(filename.endswith(".txt"))
    print(filename.endswith(".exe"))
    print("匹配多种可能，传入多个，必须是元组")
    filenames = os.listdir('../')
    print([name for name in filenames if name.endswith(('.py', '.c'))])

