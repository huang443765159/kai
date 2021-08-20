a = [1, 2, 3, 4]
b = [2, 3, 4, 5, 6]
c = [i * j for i in a for j in b]
print(c)


c = [i for i in zip(a, b)]
print(c)
