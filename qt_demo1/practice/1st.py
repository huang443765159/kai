up = b'Z\x1a{\x15\x00\x00\x01\x01'
down = b'X:{\x15\xff\x7f\x02\x05'
buttons = {'A': (1, 1), 'b': (1, 2), 'x': (1, 0), 'y': (1, 3), 'LB': (1, 4), 'RB': (1, 5),
           'LT': (1, 6), 'RT': (1, 7), 'back': (1, 8), 'start': (1, 9),
           'UP': (128, 2, 5), 'Down': (127, 2, 5), 'Left': (128, 2, 4), 'Right': (127, 2, 4),
           'L_rocker_l': (128, 2, 0), 'L_rocker_r': (127, 2, 0), 'L_rocker_u': (128, 2, 1),
           'L_rocker_d': (127, 2, 1), 'R_rocker_l': (128, 2, 2), 'R_rocker_r': (127, 2, 2),
           'R_rocker_u': (128, 2, 3), 'R_rocker_d': (127, 2, 3)}
new_buttons = {value: key for key, value in buttons.items()}
print(new_buttons)


def search_button(one_bytes, one_dict=buttons):
    a = one_bytes[-1]
    b = one_bytes[-2]
    c = one_bytes[4]
    d = one_bytes[-3]
    # button = list(buttons.keys())[list(buttons.values()).index([b, a])]
    # button1 = list(buttons.keys())[list(buttons.values()).index([d, b, a])]
    if c == 1 and d == 0:
        button = list(buttons.keys())[list(buttons.values()).index([b, a])]
        print(button + ' pressed')
    elif c == 0:
        print(button + ' released')
    elif c == 255:
        button1 = list(buttons.keys())[list(buttons.values()).index([d, b, a])]
        print(button1 + ' pressed')
    elif c == 1:
        button1 = list(buttons.keys())[list(buttons.values()).index([d, b, a])]
        print(button1 + ' pressed')


search_button(down, buttons)


