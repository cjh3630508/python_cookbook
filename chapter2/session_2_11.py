import re

if __name__ == '__main__':
    print("-- 删除字符串中不需要的字符 --")

    print("-- 删除开始和结尾字符 strip,lstrip rstrip --")
    str = "   开头和结尾空白  "
    print("strip [{}]".format(str.strip()))
    print("lstrip [{}]".format(str.lstrip()))
    print("rstrip [{}]".format(str.rstrip()))
    str = "---开头和结尾特殊字符==="
    print("strip [{}]".format(str.strip('-=')))
    print("lstrip [{}]".format(str.lstrip('-=')))
    print("rstrip [{}]".format(str.rstrip('-=')))
    print("\n")

    print("-- replace 普通替换 --")
    print("替换-、= [{}]".format(str.replace('-', '').replace('=', '')))
    print("\n")

    print("-- 正则替换 sub --")
    print("正则替换-、= [{}]".format(re.sub(r'[-=]', '', str)))
