import random


def make_list(length):
    a = list()
    for i in range(length):
        a.append(random.randint(20, 100))
    return a


def is_odd(list_1):
    odd_list = list()
    for i in list_1:
        if i % 2 != 0:
            odd_list.append(i)
            # continue
    return odd_list


def is_even(random_list):
    even_list = list()
    for b in random_list:
        if b % 2 == 0:
            even_list.append(b)
    return even_list


def is_prime(temp_list):
    prime_list = list()
    for x in temp_list:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            prime_list.append(x)
    return prime_list


def get_sum(odd_list, even_list, prime_list):
    finally_list = list()
    for i in odd_list:
        for x in even_list:
            for z in prime_list:
                if 100 < i + x + z < 200:
                    finally_list.append([i, x, z])
    return finally_list


def run():
    list_2 = make_list(10)
    print(list_2)
    list_3 = is_odd(list_2)
    print(list_3)
    list_4 = is_even(list_2)
    print(list_4)
    list_5 = is_prime(list_2)
    print(list_5)
    bingo_list = get_sum(list_3, list_4, list_5)
    print(bingo_list)


run()