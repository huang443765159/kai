import random


def make_flowers_dict(length):
    flowers_dict = {}
    for i in range(length):
        petal_number = random.randint(1, 20)
        flowers_dict['flower' + str(i)] = petal_number
    # print(flowers_dict)
    return flowers_dict


# a = make_flowers_dict(length=10)
# print(a)


# def search_expensive_flower(expensive_flower):
    # one_flower = list()想返还列表，逻辑错误
    # max_value = 0
    # for flower, petal in expensive_flower.items():
        # if max_value < petal:
            # max_value = petal
            # expensive_flower[flower] = petal 强制改写，错误，总想把数给返还回来，错误
            # one_flower.append([flower, petal])
    # return one_flower


def search_expensive_flower(all_flowers):
    temp_max_name = ''
    temp_max_value = 0

    for flower_name, flower_value in all_flowers.items():
        if temp_max_value < flower_value:
            temp_max_value = flower_value
            temp_max_name = flower_name
    # PLAN 1
    # one_flower = {temp_max_name: temp_max_value}可以返还字典
    # return one_flower

    # PLAN 2
    return temp_max_name, temp_max_value


a = make_flowers_dict(length=10)
b = search_expensive_flower(a)
print(b)