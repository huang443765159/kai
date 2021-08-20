a = [3, 6, 2, 7, 18]
b = len(a)
for i in range(b-1):
    for x in range(b-1-i):
        while a[x] > a[x+1]:
            a[x], a[x+1] = a[x+1], a[x]
print(a)
# 本质是把临近的两个单位做比较，最后一次的时候是把最小的数移动到第二个为止，然后第一和第二做比较
# 长度是几，就循环几-1遍


import random


def make_list(length, num_s, num_e):
    a = list()
    for i in range(length):
        a.append(random.randint(num_s, num_e))
    return a


def sort_the_list(num_list):
    b = len(num_list)
    for i in range(b-1):
        for x in range(b-1-i):
            if num_list[x] < num_list[x+1]:
                num_list[x], num_list[x+1] = num_list[x+1], num_list[x]
    return num_list


def run1():
    temp_list = make_list(3, 10, 100)
    print(temp_list)
    true_list = sort_the_list(temp_list)
    print(true_list)


def run2():
    temp_list = make_list(5, 29, 77)
    print(temp_list)
    true_list = sort_the_list(temp_list)
    print(true_list)


run2()

a = list()
for i in range(10):
    a.append([random.randint(0, 10), random.randint(10, 20)])

b = sorted(a, key=lambda x: x[1], reverse=True)  # 从第二个元素开始判断，从大到小排列
print(b)
