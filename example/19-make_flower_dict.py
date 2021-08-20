import random


def make_list(length, num_s, num_e):
    num_list = list()
    for i in range(length):
        num_list.append(random.randint(num_s, num_e))
    return num_list


def make_dict(length):
    num_dict = dict()
    for i in range(length):
        petal_number = make_list(5, 10, 100)
        num_dict['flower' + str(i)] = petal_number
    return num_dict


def search_exp_flower(flower_dict):
    temp_key = ''
    temp_value = [0]
    for key, value in flower_dict.items():
        if temp_value < value:
            temp_value = value
            temp_key = key
    exp_flower = {temp_key: temp_value}
    return exp_flower


def search_max_petal(one_flower):
    for petal in one_flower.values():
        petals = 0
        for number in petal:
            petals += number
        return petals


def run():
    petal_list = make_list(5, 10, 100)
    print(petal_list)
    flowers_dict = make_dict(5)
    print(flowers_dict)
    expensive_flowers = search_exp_flower(flowers_dict)
    print('The expensive flower is {} '.format(expensive_flowers))
    max_petal = search_max_petal(expensive_flowers)
    print("The expensive flower's petals are {} ".format(max_petal))


run()
