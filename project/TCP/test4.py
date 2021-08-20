import sdl2.ext
from Temp.math.button_dict import axis, get_value
import time


sdl2.SDL_Quit(sdl2.SDL_INIT_JOYSTICK)
sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
#  初始化
sdl2.joystick.SDL_NumJoysticks()
sdl2.SDL_JoystickOpen(0)
while 1:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_JOYAXISMOTION:
            # print([event.jaxis.axis, event.jaxis.value])
            value = get_value(event.jaxis.value)
            joy_axis = [event.jaxis.axis, value]
            for key, value in axis.items():
                if joy_axis == value:
                    print(key)
            if event.jaxis.axis == 4 or event.jaxis.axis == 5:
                if event.jaxis.value == -32768:
                    print(axis[event.jaxis.axis], False)
                else:
                    print(axis[event.jaxis.axis], True)
    time.sleep(0.01)



