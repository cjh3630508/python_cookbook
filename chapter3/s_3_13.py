from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

if __name__ == '__main__':
    print("-- 计算最后一个周五的日期 --")
    print()

    d = datetime.now()
    print("day={}".format(d))
    print("next friday={}".format(d + relativedelta(weekday=FR)))
    print("last friday={}".format(d + relativedelta(weekday=FR(-1))))