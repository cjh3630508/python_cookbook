from datetime import datetime
from pytz import timezone

if __name__ == '__main__':
    print("-- 结合时区的日期操作 --")
    print()

    """
    使用 pytz 模块
    """
    now = timezone('Asia/Shanghai').localize(datetime.now())
    print("now is {}".format(now))
    print("now in US/Central {}".format(now.astimezone(timezone('US/Central'))))
