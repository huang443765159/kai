def is_leap_number(number):
    active = True
    for is_leap in range(2, number):
        if number % is_leap == 0:
            active = False
    if active:
        b = 1
        for i in range(1, number + 1):
            b = b * i
        print(b)


is_leap_number(7)

#
def is_prime_num(num):
    active = True
    for i in range(2, num):
        if num % i == 0:
            active = False
    return active


def get_qud(num):
    b = 1
    result = ''
    for i in range(1, num + 1):
        one_num = is_prime_num(num)
        if one_num:
            b *= i
            result = b
    return result


if __name__ == '__main__':

    number = 7
    bingo = get_qud(number)
    print(bingo)








