import re


a = 'hello, I am your father, a=1'

# 分割单个符号
b = re.split(',', a)
print(b)

# 分割多个符号
c = re.split('[,=]', a)
d = re.split(r'=|,|,\s', a)
print(c)
print(d)


# 读取文件内容
with open('example.txt') as f:
    for line in f.readlines():
        info = re.findall(r'bot_id=\w, chem_id=\w, chem_level=\w', line)
        print(info)


import os
import re


TAR_FILE = os.path.expanduser('~/Documents/CODES')
with open(os.path.join(TAR_FILE, 'XYZSwitches3', 'setup.py'), 'r') as f:
    lines = f.read()
    print(lines)
    b = re.findall(r'version+=(.+)', lines)
    print(b[0])


c = 'sasa=asdads.asdad'

b = re.findall(r'.+=(.+)', c)
d = re.findall(r'.+=(.+)\.', c)
print(b)
print(d)


a = '123.123    456.789   '
print(a.rstrip())  # 去除末尾空格
print(a.rsplit())  # 去除所有空格
