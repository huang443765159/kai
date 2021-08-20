import random


def make_list(num_start, num_end):
    num_list = list()
    while 1:
        num = random.randint(num_start, num_end)
        if num not in num_list:
            num_list.append(num)
        if len(num_list) == num_end:
            break
    return num_list


def search_idx(list_1, target):
    for idx, num in enumerate(list_1):
        if num == target:
            print(idx)
    if target not in list_1:
        print(len(list_1))


if __name__ == '__main__':

    new_list = make_list(0, 10)
    print(new_list)
    search_idx(new_list, 11)
    # bingo = search_idx(new_list, 3)