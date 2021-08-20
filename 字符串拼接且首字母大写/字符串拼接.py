import re

a = input()

b = re.split(' |, |;', a)
print(b)
c = list(map(lambda x: x.title(), b))
print(c)

msg = str()

for i in c:
    msg += i + ' '
print(msg)