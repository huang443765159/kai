import random


a = list()
b = 1
while b <= 1000:  # length
    c = random.randint(1, 1000)  # all_number
    if c not in a:
        a.append(c)
        b += 1
print(a)
#  2
while 1:
    c = random.randint(1, 1000)
    if c not in a:
        a.append(c)
    if len(a) == 1000:
        break





# y = list()
# for i in range(1000):
#     c = a.pop()
#     y.append(13473989000 + c)
# print(y)
# z = len(y)
# for i in range(z):
#     if y[i] == 13473989444:
#         print(i)


#  2
a = random.sample(range(1, 101), 100)
#  range, all_number
print(a)

import random


def make_list(length, all_number):
    number_list = list()
    b = 1
    while b <= length:
        num = random.randint(1, all_number)
        if num not in number_list:
            number_list.append(num)
            b += 1
    return number_list


def make_phone_list(list_1):
    phone_list = list()
    b = len(list_1)
    for i in range(b):
        c = list_1.pop()
        phone_list.append(13473989800 + c)
    return phone_list


final_list = make_list(100, 100)
num_list = make_phone_list(final_list)
print(num_list)
