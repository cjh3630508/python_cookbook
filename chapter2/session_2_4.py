import re


def is_match_reg(pat: re.Pattern, str):
    print("[{}] match [{}] : {}".format(str, pat.pattern, pat.match(str) != None))


if __name__ == '__main__':
    print("-- 字符串匹配和搜索 --")
    print("预编译正则")
    pat = re.compile(r'\d+/\d+/\d+')
    is_match_reg(pat, "2020/08/23")
    is_match_reg(pat, "Aug 23/2020")
    print("findall 查找所有匹配字符串")
    print(pat.findall("today is 2020/08/23, tomorrow is 2020/08/24"))
    print("分组")
    pat = re.compile(r'(\d+)/(\d+)/(\d+)')
    match = pat.match("2020/08/23")
    print(match)
    print(match.groups())
    year, month, day = match.groups()
    print("{}-{}-{}".format(year, month, day))
    
