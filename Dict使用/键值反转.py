a = {'a': 1,
     'b': 2,
     'c': 3}


b = zip(a.keys(), a.values())  # zip函数打包的变量只能使用一次

c = dict(b)  # 赋值之后 b则为空数据了
print(c)

d = list(b)  # 空列表
print(d)
