import js2py
import time


"""
pip3 install js2py
不需要依赖，且速度很快，55ms
"""

ts_start = time.time()
with open('add.js', 'r', encoding='UTF-8') as file:
    result = file.read()

context = js2py.EvalJs()
context.execute(result)

result = context.add(1, 2)
print(result, time.time() - ts_start)
