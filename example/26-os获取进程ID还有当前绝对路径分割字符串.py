import os

print(os.getpid())
a = os.path.dirname(os.path.abspath(__file__))
print(a)
c = a.split('/')
print(c)
x = len(c)
print(x)
for i in range(x):
    if c[i] == 'huangkai':
        print(i)
d = c[0] + '/' + c[1] + '/' + c[2]
print(d)
