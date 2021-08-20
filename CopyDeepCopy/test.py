import copy
'''
直接复制 a=b   同一内存，只是调用变量而已
浅拷贝  a=b.copy()  子对象为同一内存
深拷贝  a=copy.deepcopy(b)  需要import copy  完全独立，两个内存
'''

a = [1, 2, 3, 4, [5, 6]]
b = a
# a或者b其一改变，都跟随改变
c = a.copy()  # c = copy(a)
# a或者c的子对象[5, 6]跟随改变，父对象独立不改变
d = copy.deepcopy(a)
# a,d随便改变，都没影响，为两个完全独立对象
