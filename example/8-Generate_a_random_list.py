# import random
# rand_list = []
# for i in range(10):
#     rand_list.append(random.randint(1, 101))
#
# print(rand_list)

import random
print([random.randint(1, 100) for x in range(10)])


# import random
# 随机生成字典

a = {}
for i in range(5):
    v = random.randint(1, 10)
    a[str(i)] = v
print(a)




