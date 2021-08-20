import random


def make_random_list(length, range_start, range_end):
    new_list = list()
    for x in range(length):
        new_list.append(random.randint(range_start, range_end))
    return new_list


def search_100(list_1, list_2, list_3):
    bingo_list = list()
    for num_1 in list_1:
        for num_2 in list_2:
            for num_3 in list_3:
                if num_1 + num_2 + num_3 == 100:
                    bingo_list.append([num_1, num_2, num_3])
    return bingo_list


if __name__ == '__main__':

    # MAKE LIST
    list_a = make_random_list(length=10, range_start=1, range_end=100)
    list_b = make_random_list(length=10, range_start=1, range_end=100)
    list_c = make_random_list(length=10, range_start=1, range_end=100)

    # SEARCH 100 LIST
    result_list = search_100(list_a, list_b, list_c)

    # REPORT RESULT
    print('Found {} list with bingo'.format(len(result_list)))
    # print(*result_list, sep='\n')
    for i in range(len(result_list)):
        print('<{}> {}'.format(i, result_list[i]))
