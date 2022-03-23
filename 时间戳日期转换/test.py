import time
import datetime


# 时间戳转换日期
a = datetime.datetime.fromtimestamp(int(str(1647920707002)[:10]))
print(a)

# 日期转换时间戳
b = datetime.datetime.now()
b = str(b)[:19]
b_array = time.strptime(str(b), "%Y-%m-%d %H:%M:%S")
b_stamp = time.mktime(b_array)
print(b_stamp)


c = datetime.date.today()
c = str(c) + ' 0:0:0'
c_array = time.strptime(c, '%Y-%m-%d %H:%M:%S')
c_stamp = time.mktime(c_array)
print(c_stamp)


def get_time_stamp(s_time: str, end_time: str) -> list:
    s_array = time.strptime(s_time, "%Y-%m-%d %H:%M:%S")
    e_array = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    s_stamp = time.mktime(s_array)
    e_stamp = time.mktime(e_array)
    return [s_stamp, e_stamp]
