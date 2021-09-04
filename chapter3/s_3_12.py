from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

if __name__ == '__main__':
    print("-- 基本的日期与时间转换 --")
    print()

    print("-- 使用 datetime 模块的 timedelta --")
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c)
    print("c.days={},c.seconds={}".format(c.days, c.seconds))

    print("-- 使用 datetime  --")
    a = datetime(2012, 9, 23)
    print("a={}".format(a))
    print("a+10天={}".format(a + timedelta(days=10)))
    b = datetime(2012, 12, 21)
    print("b={}".format(b))
    d = b - a
    print("b-a={}".format(d))
    print("now={}".format(datetime.today()))

    print("-- 使用 dateutil 计算复杂日期操作 --")
    print("a+一个月={}".format(a + relativedelta(months=1)))
