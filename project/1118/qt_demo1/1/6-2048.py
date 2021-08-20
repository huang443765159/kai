up = b'Z\x1a{\x15\x00\x00\x01\x00'
down = b'X:{\x15\xff\x7f\x02\x05'
buttons = {(0, 1, 1): 'A', (0, 1, 2): 'B', (0, 1, 0): 'X', (0, 1, 3): 'Y', (0, 1, 4): 'LB', (0, 1, 5): 'RB',
            (0, 1, 6): 'LT', (0, 1, 7): 'RT', (0, 1, 8): 'back', (0, 1, 9): 'start', (128, 2, 5): 'UP',
            (127, 2, 5): 'Down', (128, 2, 4): 'Left', (127, 2, 4): 'Right', (128, 2, 0): 'L_rocker_l',
            (127, 2, 0): 'L_rocker_r', (128, 2, 1): 'L_rocker_u', (127, 2, 1): 'L_rocker_d', (128, 2, 2): 'R_rocker_l',
            (127, 2, 2): 'R_rocker_r', (128, 2, 3): 'R_rocker_u', (127, 2, 3): 'R_rocker_d'}
state = {(0, 2, 5): 'Up or Down', (0, 2, 4): 'Left or Right', (0, 2, 0): 'L_rocker_r or L_rocker_l',
         (0, 2, 1): 'L_rocker_u or L_rocker_d', (0, 2, 2): 'R_rocker_r or R_rocker_l',
         (0, 2, 3): 'R_rocker_u or R_rocker_d'}


def search_button(byte, button_dict, button_state):
    num1 = byte[-1]
    num2 = byte[-2]
    num3 = byte[-3]
    num4 = byte[4]
    button_name = (num3, num2, num1)
    if num4 == 1 and button_name in button_dict.keys():
        print(button_dict[button_name] + ' pressed')
    elif num4 == 255 and button_name in button_dict.keys():
        print(button_dict[button_name] + ' pressed')
    elif num4 == 0 and button_name in button_dict.keys():
        print(button_dict[button_name] + ' released')
    elif num4 == 0 and button_name in button_state:
        print(button_state[button_name] + ' released')


if __name__ == '__main__':
    search_button(up, buttons, state)
