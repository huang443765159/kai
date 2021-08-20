def p_models(a, b):
    while a:
        c = a.pop()
        b.append(c)


def n_p_models(b):
    for b1 in b:
        print(b1)


a = ['a', 'b', 'c']
b = []

p_models(a, b)
n_p_models(b)
# 两种方式把两个列表调换并把里面的数字打印出来

a = ['a', 'b', 'c']
b = []
while a:
    c = a.pop()
    b.append(c)
for b1 in b:
    print(b1)


from random import randint


a = list()
for i in range(10):
    a.append({i: randint(0, 10)})
print(a)
# 创建列表里面随机字典