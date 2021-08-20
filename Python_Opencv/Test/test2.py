import numpy as np


a = list()
for i in range(9600):
    a.append(i)
b = np.array(a).reshape(64, 150)


c = list(b)

for idx, one_list in enumerate(c):
    if idx % 2 != 0:
        c[idx] = list(reversed(one_list))
d = np.array(c)
print(d)
print(d.T)
