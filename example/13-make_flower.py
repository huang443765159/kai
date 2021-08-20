import random


def make_flowers_dict(length):
    flowers_dict = {}
    for i in range(length):
        petal_number = random.randint(1, 20)
        flowers_dict['flower' + str(i)] = petal_number
    # print(flowers_dict)
    return flowers_dict


def search_expensive_flower(all_flowers):
    temp_max_name = ''
    temp_max_value = 0

    for flower_name, flower_value in all_flowers.items():
        if temp_max_value < flower_value:
            temp_max_value = flower_value
            temp_max_name = flower_name
     # PLAN 1
    one_flower = {temp_max_name: temp_max_value}
    return one_flower

    # PLAN 2
    # return temp_max_name, temp_max_value


def search_cheap_flower(flower_dict):
    temp_key = ''
    temp_value = list(flower_dict.values())[0]
    for flower_name, petal_number in flower_dict.items():
        if temp_value > petal_number:
            temp_value = petal_number
            temp_key = flower_name
    one_flower = {temp_key: temp_value}
    return one_flower


def search_avg(flower_dict):
    sum_numbers = 0
    for petal_number in flower_dict.values():
        sum_numbers += petal_number
    avg_petal_number = sum_numbers / len(flower_dict)
    return avg_petal_number


a = make_flowers_dict(length=10)
this_flower = search_expensive_flower(a)
cheap_flower = search_cheap_flower(a)
ave_petal = search_avg(a)
print(a)
print('{} is the exp flower'.format(this_flower))
print('{} is the chp flower'.format(cheap_flower))
print('The petals avg is {} '.format(ave_petal))
