import re
import os


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


a = """
commit d6451a20fe70f71556cb0507bf54a29200cd8e86
Author: huangkai <443765159@qq.com>
Date:   Thu Feb 4 15:47:56 2021 +0800

    1：化学泵、高压水、风机、排水泵的开关驱动
       单模块都包含独立server和端口号
    2：含Gui测试用例"""

b = '(?<=commit ).*'
print(re.findall(b, a))

a = 'b7cc146b779160ff01fe15f1b67973348dfead9c	refs/heads/master'
b = re.split(r'[ ]', a)
c = re.findall(r'(.+)refs', a)[0]
print(c)
