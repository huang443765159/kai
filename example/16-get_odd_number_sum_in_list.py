import random
# 求随机列表里面奇数的和
# 先造列表，然后求奇数，然后求和


def make_list(length):
    new_list = list()
    for i in range(length):
        new_list.append(random.randint(1, 100))
    return new_list


def search_odd_num(all_num_list):
    odd_list = list()
    for num in all_num_list:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list


def sum_odd_num(list_1):
    b = 0
    for num in list_1:
        b = b + num
    return b


num_list = make_list(10)
# print(num_list)
odd_number_list = search_odd_num(num_list)
sum_odd_number = sum_odd_num(odd_number_list)
print(odd_number_list)
print('The prime number sum is {}'.format(sum_odd_number))
