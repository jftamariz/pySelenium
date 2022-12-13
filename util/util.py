from re import sub, search
from decimal import Decimal
import datetime


def ge_now_timestamp():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def get_now_datetime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def convert(m):
    r = 1.0
    if "£" in m:
        r = 1.28  # Make sure to check this (conversion rate between pounds and usd)
    z = 0
    if "B" in m:
        z = 9
    if "M" in m:
        z = 6
    if "K" in m:
        z = 3
    if "." in m:
        z -= len(sub(r'[^\d.]', '', m).split(".")[1])
    if not bool(search(r'\d', m)):
        m = "0"
    value = Decimal(sub(r'[^\d]', '', m))

    n = int(value * Decimal(r) * (10 ** (z)))
    return n