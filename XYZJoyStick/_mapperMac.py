import sdl2.ext

btn_mapper = {0: 'A', 1: 'B', 2: 'X', 3: 'Y', 4: 'RETURN', 5: 'POWER', 6: 'STOP',
              9: 'LB', 10: 'RB', 11: 'UP', 12: 'DOWN', 13: 'LEFT', 14: 'RIGHT',
              7: 'RR', 8: 'LR'}

axis_mapper = {0: 'STICK_L_X', 1: 'STICK_L_Y', 2: 'STICK_R_X', 3: 'STICK_R_Y', 5: 'LT', 4: 'RT'}
axis_memory = {'STICK_L_X': 0, 'STICK_L_Y': 0, 'STICK_R_X': 0, 'STICK_R_Y': 0, 'LT': 0, 'RT': 0}

hat_mapper = {8: 'LEFT', 2: 'RIGHT', 1: 'UP', 4: 'DOWN', 0: 'RELEASE', 9: 'LEFT_UP', 3: 'RIGHT_UP', 12: 'LEFT_DOWN', 6: 'RIGHT_DOWN'}
hat_memory = None


def mapper_parse(event, axis_as_btn, axis_threshold):
    global btn_mapper, axis_mapper, axis_memory, hat_mapper, hat_memory
    event_type = event.type
    reply = (None, None, None)
    if event_type == sdl2.SDL_JOYAXISMOTION:
        axis_key = event.jaxis.axis
        axis_name = axis_mapper[axis_key]
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

    elif event_type in [sdl2.SDL_JOYBUTTONDOWN, sdl2.SDL_JOYBUTTONUP]:
        btn_name = btn_mapper[event.jbutton.button]
        btn_status = True if event_type == sdl2.SDL_JOYBUTTONDOWN else False
        reply = ('BUTTON', btn_name, btn_status)

    elif event_type == sdl2.SDL_JOYHATMOTION:
        btn_name = hat_mapper[event.jhat.value]
        if btn_name == 'RELEASE':
            btn_name = hat_memory
            btn_state = False
        else:
            hat_memory = btn_name
            btn_state = True
        reply = ('BUTTON', btn_name, btn_state)
    else:
        print('Unknown', event_type)
    return reply
