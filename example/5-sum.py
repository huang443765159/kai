def sum_number(number):
    a = 0
    for i in range(0, number + 1):
        a += i
        print(a)


sum_number(6)


import random


def make_list(length):
    number_list = []
    for i in range(length):
        number_list.append(random.randint(1, 100))
    return number_list


def sum_number(list1):
    b = 0
    for number in list1:
        b += number
    print(b)


new_list = make_list(10)
sum_number(new_list)
print(new_list)
