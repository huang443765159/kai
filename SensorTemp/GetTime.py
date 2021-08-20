

def get_distance(temp, dis=1):
    c = 331.4 + 0.607 * temp
    time = dis * 2000 / c
    new_dis = time * 340 / 2000
    print(new_dis)
    return c, (new_dis-dis) / dis * 100, new_dis


if __name__ == '__main__':

    temp1 = 25
    # temp2 = 30
    c1, per1, act_dis = get_distance(temp1)
    # c2, per2 = get_distance(temp2)
    print('speed={}m/s, per={}%, dis={}'.format(c1, per1, act_dis))
    # print('speed={}m/s, per={}%'.format(c2, per2))
