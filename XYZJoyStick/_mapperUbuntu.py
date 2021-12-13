import sdl2.ext

# btn_mapper = {0: 'A', 1: 'B', 3: 'X', 4: 'Y', 15: 'RETURN', 11: 'STOP', 6: 'LB', 7: 'RB', 16: 'POWER'}
#
# axis_mapper = {0: 'STICK_L_X', 1: 'STICK_L_Y', 2: 'STICK_R_X', 3: 'STICK_R_Y', 4: 'RT', 5: 'LT'}
# axis_memory = {'STICK_L_X': 0, 'STICK_L_Y': 0, 'STICK_R_X': 0, 'STICK_R_Y': 0, 'LT': 0, 'RT': 0}
#
# hat_mapper = {8: 'LEFT', 2: 'RIGHT', 1: 'UP', 4: 'DOWN', 0: 'RELEASE',  9: 'LEFT_UP', 3: 'RIGHT_UP', 12: 'LEFT_DOWN', 6: 'RIGHT_DOWN'}
# hat_memory = None

btn_mapper = {0: 'A', 1: 'B', 2: 'X', 3: 'Y', 6: 'RETURN', 7: 'STOP', 4: 'LB', 5: 'RB', 10: 'POWER'}

axis_mapper = {0: 'STICK_L_X', 1: 'STICK_L_Y', 3: 'STICK_R_X', 4: 'STICK_R_Y', 5: 'RT', 2: 'LT'}
axis_memory = {'STICK_L_X': 0, 'STICK_L_Y': 0, 'STICK_R_X': 0, 'STICK_R_Y': 0, 'LT': 0, 'RT': 0}

hat_mapper = {8: 'LEFT', 2: 'RIGHT', 1: 'UP', 4: 'DOWN', 0: 'RELEASE',  9: 'LEFT_UP', 3: 'RIGHT_UP', 12: 'LEFT_DOWN', 6: 'RIGHT_DOWN'}
hat_memory = None


def mapper_parse(event, axis_as_btn, axis_threshold):
    global btn_mapper, axis_mapper, axis_memory, hat_mapper, hat_memory
    event_type = event.type
    reply = (None, None, None)

    # AXIS : STICK_LEFT, STICK_RIGHT, LT, RT
    if event_type == sdl2.SDL_JOYAXISMOTION:
        axis_name = axis_mapper[event.jaxis.axis]
        axis_value = event.jaxis.value
        if axis_as_btn:
            if abs(axis_value) > axis_threshold:
                axis_value = 1 if axis_value > 0 else -1
            else:
                axis_value = 0
            if axis_name in ['LT', 'RT']:
                axis_value = 0 if axis_value == -1 else 1
            if axis_memory[axis_name] != axis_value:
                axis_memory[axis_name] = axis_value
                reply = ('AXIS', axis_name, axis_value)
        else:
            reply = ('AXIS', axis_name, axis_value)

    # BUTTONS_HAT: ↑/↓/←/→
    elif event_type == sdl2.SDL_JOYHATMOTION:
        btn_name = hat_mapper[event.jhat.value]
        if btn_name == 'RELEASE':
            btn_name = hat_memory
            btn_state = False
        else:
            hat_memory = btn_name
            btn_state = True
        reply = ('BUTTON', btn_name, btn_state)

    # BUTTONS : LB/RB, A/B/X/Y, Return/Stop
    elif event_type in [sdl2.SDL_JOYBUTTONDOWN, sdl2.SDL_JOYBUTTONUP]:
        btn_name = btn_mapper[event.jbutton.button]
        btn_state = True if event_type == sdl2.SDL_JOYBUTTONDOWN else False
        reply = ('BUTTON', btn_name, btn_state)

    else:
        print('Unknown', event_type)

    return reply


'''
    * 树莓派连接XBOX手柄，获取正确MAPPER的方法 *

【首次配对】打开手柄电源，按下蓝牙配对键，进入快闪对配状态，在此方式下进行配对，将进入D模式
【切换D模式至X模式】配对成功后，按住手柄电源直至关闭，然后重新打开手柄电源，让树莓派自动连接到手柄，进入X模式
【此后：永久为X模式】

备注：如果在手柄进入X模式的情况下，有过树莓派蓝牙被关闭的情况，则需要重新使用上述流程以进入X模式

'''