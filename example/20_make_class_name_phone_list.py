'''
1-长度由length决定的
2-输入的是一个随机手机号，然后对应一个名字，
3-输出的是一个名字对应手机号的列表
'''


import random


def make_list(length):
    name_list = list()
    for i in range(length):
        name_list.append(('tom' + str(i), 13473980000+random.randint(0, 10000)))
    return name_list


def search_name(name_list):
    phone_num = name_list[random.randint(0, len(name_list) - 1)][1]
    print(phone_num)
    for person in name_list:
        for number in person:
            if number == phone_num:
                return person[0], number


def run():
    names_list = make_list(10)
    print(names_list)
    the_person, phone = search_name(names_list)
    print('phone = {}'.format(phone), 'and the name is {} '.format(the_person))


run()
