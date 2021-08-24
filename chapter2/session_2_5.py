import re
from calendar import month_abbr


def change_date(m: re.Match):
    mon_name = month_abbr[int(m.group(1))]
    return "{} {} {}".format(m.group(2), mon_name, m.group(3))


if __name__ == '__main__':
    print("-- 字符串搜索与替换 --")
    print("-- 简单字符串使用 str.replace 即可 --")
    text = "year, but on, but year, but no, but year"
    print("text is : ")
    print(text)
    print("after replace,text is :")
    print(text.replace("year", "yep"))

    print("-- re.sub 函数 --")
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print("text is :")
    print(text)
    print("正则分组修改位置, 第二个正则， \3 表示捕获的分组位置")
    print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

    print("-- 使用替换回调函数 --")
    date_pat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(date_pat.sub(change_date, text))
