from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    '''
    计算月份的日期范围
    :returns (start_date, end_date) 起始（包含）和终止（不包含）日期
    '''
    if start_date is None:
        start_date = date.today()
    start_date = start_date.replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


if __name__ == '__main__':
    print("-- 计算当前月份的日期范围 --")
    start_day, end_day = get_month_range()
    one_day = timedelta(days=1)
    print("-- 普通遍历 --")
    while start_day < end_day:
        print(start_day)
        start_day += one_day

    print("-- 使用生成器 --")
    start_day, end_day = get_month_range()
    for day in date_range(start_day, end_day, timedelta(days=1)):
        print(day)
