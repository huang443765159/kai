buttons = {0: 'A',
           1: 'B',
           2: 'X',
           3: 'Y',
           4: 'Return',
           5: 'Charging',
           6: 'Stop',
           7: 'Right_rock',
           8: 'Left_rock',
           9: 'LB',
           10: 'RB',
           11: 'Up',
           12: 'Down',
           13: 'Left',
           14: 'Right'}

axis = {4: 'LT',
        5: 'RT',
        'R-r-u pressed': [3, -2],
        'R-r-d pressed': [3, 2],
        'R-r-l pressed': [2, -2],
        'R-r-r pressed': [2, 2],
        'R-r-u released': [3, -1],
        'R-r-d released': [3, 1],
        'R-r-l released': [2, -1],
        'R-r-r released': [2, 1],
        'L-r-u pressed': [1, -2],
        'L-r-d pressed': [1, 2],
        'L-r-l pressed': [0, -2],
        'L-r-r pressed': [0, 2],
        'L-r-u released': [1, -1],
        'L-r-d released': [1, 1],
        'L-r-l released': [0, -1],
        'L-r-r released': [0, 1]}


def get_value(value):
    temp_value = ''
    if 0 < value < 3200:
        temp_value = 1
    elif value > 3200:
        temp_value = 2
    elif 0 > value > -3200:
        temp_value = -1
    elif value < -3200:
        temp_value = -2
    return temp_value



