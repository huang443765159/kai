import random


# PRIME_NUM
def search_prime_num(num1, num2):
    prime_list = list()
    for x in range(num1, num2):
        active = True
        for y in range(2, x):
            if x % y == 0:
                active = False
        if active:
            prime_list.append(x)
    return prime_list


# LEAP_YEAR
def is_leap_year(one_year):
    result = False
    if one_year % 4 == 0:
        if one_year % 100 == 0:
            if one_year % 400 == 0:
                result = True
        else:
            result = True
    return result


def search_leap_year(s_year, e_year):
    leap_years = list()
    for one_year in range(s_year, e_year + 1):
        result = is_leap_year(one_year=one_year)
        if result:
            leap_years.append(one_year)
    return leap_years


# SEARCH_FLOWER
def make_flowers(length=15):
    flowers = dict()
    for i in range(length):
        flowers['flower' + str(i)] = random.randint(10, 50)
    return flowers


def search_flower(flowers: dict):
    flowers_copy = sorted(flowers.items(), key=lambda x: x[1], reverse=True)
    return flowers_copy[0], flowers_copy[-1]


if __name__ == '__main__':

    prime_num = search_prime_num(10, 40)
    print(f'质数： {prime_num}')

    leap_years1 = search_leap_year(1000, 2000)
    print(f'闰年：{leap_years1}')

    max_flower, min_flower = search_flower(flowers=make_flowers())
    print(max_flower, min_flower)
