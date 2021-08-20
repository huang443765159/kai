

def get_distance(temp, time=20):
    c = 331.4 + 0.607 * temp
    print(c)
    dis = c * time / 2000
    return c, dis


if __name__ == '__main__':

    temp1 = -10
    temp2 = 25
    c1, dis1 = get_distance(temp1)
    c2, dis2 = get_distance(temp2)
    print('speed={}m/s, dis={}m'.format(c1, dis1))
    print('speed={}m/s, dis={}m'.format(c2, dis2))
