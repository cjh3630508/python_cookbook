import re


def printMatchResult(reg, str):
    print("原始字符串：[{}]".format(str))
    print("正则表达式：{}".format(reg))
    print("匹配结果：")
    print(re.findall(reg, str))
    print("\n")


if __name__ == '__main__':
    print("-- 多行匹配模式 --")
    comment1 = '/*this is a comment*/'
    comment2 = '''/*this
    is
    a
    multiline
    comment*/'''

    print("-- * 可以匹配单行注释，无法匹配多行注释 --")
    printMatchResult(r'/\*(.*?)\*/', comment1)
    printMatchResult(r'/\*(.*?)\*/', comment2)

    print("-- 修改正则，添加对 \n 的支持，(?:) 指定非捕获组，仅仅用来匹配 --")
    printMatchResult(r'/\*((?:.|\n)*?)\*/', comment1)
    printMatchResult(r'/\*((?:.|\n)*?)\*/', comment2)
