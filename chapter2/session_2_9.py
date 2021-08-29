import unicodedata

if __name__ == '__main__':
    print("-- unicode 文本标准化 unicodedata --")
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print(s1 == s2)
    print("s1 : {}".format(s1))
    print("s2 : {}".format(s2))
    print("len of s1 : {}".format(len(s1)))
    print("len of s2 : {}".format(len(s2)))
    print("ascii of s1 : {}".format(ascii(s1)))
    print("ascii of s2 : {}".format(ascii(s2)))
    print("\n")

    print("-- unicodedata normalize --")
    print("-- normalize with NFC, NFC 表示整体组成，如果可能尽量使用单一编码 --")
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print("normalize of s1 : {}".format(t1))
    print("normalize of s2 : {}".format(t2))
    print("ascii of normalize s1 : {}".format(ascii(t1)))
    print("ascii of normalize s2 : {}".format(ascii(t2)))
    print("\n")

    print("-- normalize with NFD, NFD 表示字符应该分解为多个组合字符表示 --")
    t1 = unicodedata.normalize('NFD', s1)
    t2 = unicodedata.normalize('NFD', s2)
    print("normalize of s1 : {}".format(t1))
    print("normalize of s2 : {}".format(t2))
    print("ascii of normalize s1 : {}".format(ascii(t1)))
    print("ascii of normalize s2 : {}".format(ascii(t2)))
    unicodedata.combining()
