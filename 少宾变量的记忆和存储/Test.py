import random
import time

'''
少宾变量如果是列表或者字典的话，需要把列表或者字典里的每一个值拿出来作为对比
如果拿整个列表或者字典做暂存会出现错误
'''
a = dict()
# 必须存每一个值的变量，不能用b=dict()跟a直接做比较
b = {0: None, 1: None, 2: None}

while 1:
    for i in range(3):
        a[i] = random.randint(0, 100)
        # a[i] = 1
        print('A1', a)
        if None not in a.values():
            if b[i] != a[i]:
                b[i] = a[i]
                print('A2', a)
    time.sleep(1)
