def is_prime_number(num):
    active = True
    for x in range(2, num):
        if num % x == 0:
            active = False
    if active:
        print(num)
    return active


is_prime_number(9)
