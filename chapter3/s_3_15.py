from datetime import datetime

if __name__ == '__main__':
    print("-- 字符串转为日期 --")
    print()

    """
    strptime 性能比较差
    %Y 代表 4 位数年份
    %m 代表两位数月份
    """
    date_str = '2012-09-20'
    date = datetime.strptime(date_str, '%Y-%m-%d')
    now = datetime.now()
    print("date is {}".format(date))
    print("delta with today is :{}".format(now - date))
