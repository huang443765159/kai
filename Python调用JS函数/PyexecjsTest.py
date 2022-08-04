import time


"""
pip3 install PyExecJS
还需要安装JAVA
缺点，启动比较慢,600ms
"""

import execjs

ts_start = time.time()
with open('add.js', 'r', encoding='UTF-8') as file:
    result = file.read()

context = execjs.compile(result)
result = context.call('add', 2, 3)
print(result, time.time() - ts_start)
