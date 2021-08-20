import random


def make_list(length):
    temp_list = list()
    for i in range(length):
        temp_list.append(random.randint(10, 70))
    return temp_list


def make_list_1(length):
    finally_list = list()
    for a in range(length):
        finally_list.append(make_list(5))
    return finally_list


def run():
    bingo_list = make_list_1(5)
    print(bingo_list)


def run2():
    bingo_list = make_list_1(3)
    print(bingo_list)


run2()
