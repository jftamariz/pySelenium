import datetime


def ge_now_timestamp():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def get_now_datetime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')