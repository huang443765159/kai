import random


def make_list(length, num_s, num_e):
    a = list()
    for i in range(length):
        a.append(random.randint(num_s, num_e))
    return a


def search_50(list1):
    b = len(list1)
    c = list()
    for i in range(b):  # 不能减一，因为减完就走不到最后了
        for x in range(i+1, b):
            if list1[i] + list1[x] == 50:
                c.append([list1[i], list1[x]])
    return c


list2 = make_list(40, 0, 50)
print(list2)
number = search_50(list2)
for z in number:
    print(z)


