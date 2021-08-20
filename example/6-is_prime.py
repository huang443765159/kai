def is_prime_number(num1, num2):
    for prime_number in range(num1, num2):
        active = True
        for prime_number1 in range(num1, prime_number - 1):
            if prime_number % prime_number1 == 0:
                active = False
        if active:
            print(prime_number)


# print(is_prime_number(2, 100))


def is_prime_number(num):
    active = True
    for i in range(2, num):
        if num % i == 0:
            active = False
    return active


def search_prime_num(num_start, num_end):
    for x in range(num_start, num_end):
        one_number = is_prime_number(x)
        if one_number:
            print(x)


def prime_num(num1, num2):
    for a in range(num1, num2):
        active = True
        for b in range(2, a):
            if a % b == 0:
                print(a % b)
                active = False
        if active:
            print(a)


if __name__ == '__main__':

    # search_prime_num(10, 40)
    # test(num1=10, num2=40)
    prime_num(10, 100)