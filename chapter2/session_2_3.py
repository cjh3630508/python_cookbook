from fnmatch import fnmatch
from fnmatch import fnmatchcase


def judge_str_match_pat(str, pat):
    print("{} 是 {} : {}".format(str, pat, fnmatch(str, pat)))


if __name__ == '__main__':
    print("-- 用 shell 通配符匹配字符串 --")
    print("fnmatch 提供的两个函数,fnmatch()/fnmatchcase()")
    print("fnmatch 会使用底层系统的大小写敏感规则来匹配，windows 大小写不敏感，linux 大小写敏感，如果在意可以使用 fnmatchcase")
    judge_str_match_pat('foo.txt', '*.txt')
    judge_str_match_pat('foo.txt', '?oo.txt')
    judge_str_match_pat('Dat45.csv', 'Dat[0-9]*')
