import random


def make_bottle_dict(length):
    bottles = dict()
    for i in range(length):
        value = bool(random.randint(0, 1))
        bottles['bottle' + str(i)] = value
    return bottles


def search_bottle_with_true(bottle_dict):
    temp_sum = 0
    for value in bottle_dict.values():
        if value:
            temp_sum += 1
    return temp_sum


def run1():
    # Found True Sum
    bottles_dict = make_bottle_dict(7)
    true_number = search_bottle_with_true(bottles_dict)
    print('The number of bottles with LIDS is {}.'.format(true_number))


def run2():
    # Found False Sum
    bottles_dict = make_bottle_dict(8)
    true_number = search_bottle_with_true(bottles_dict)
    print('The number of bottles with LIDS is {}.'.format(true_number))


run2()
