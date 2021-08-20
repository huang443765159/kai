import random


def make_list(length):
    the_list = list()
    for i in range(length):
        the_list.append(random.randint(0, 1))
    return the_list


def search_t_f(list_1, n):
    m = 0
    new_list = [0] + list_1 + [0]  # 前后补花就不用考虑边缘问题
    lens = len(new_list)
    for i in range(1, lens - 1):
        if new_list[i - 1] == 0 and new_list[i] == 0 and new_list[i + 1] == 0:
            new_list[i] = 1
            m += 1  # or n -= 1
    print(m)
    return n <= m  # n <= 0


if __name__ == '__main__':

    one_list = make_list(30)
    print(one_list)
    result = search_t_f(one_list, 5)
    print(result)
