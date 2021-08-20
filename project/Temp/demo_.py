import time
import sdl2.ext
from sdl2 import joystick, keyboard
import time


sdl2.SDL_Quit(sdl2.SDL_INIT_JOYSTICK)
sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK, sdl2.SDL_INIT_VIDEO)
# sdl2.SDL_QuitSubSystem(sdl2.SDL_INIT_VIDEO)
#  初始化
num = sdl2.joystick.SDL_NumJoysticks()
keysym = keyboard.SDL_Keysym()
# window = keyboard.SDL_GetKeyboardFocus()
print(keysym)
# keysym1 = keyboard.SDL_Keysym(1, 2, 3, ord("b"))
# print(keysym1.scancode)
# print(num)
joystick1 = sdl2.SDL_JoystickOpen(0)
# print(joystick1)
# joystick.SDL_JoystickClose(joystick1)
axes = joystick.SDL_JoystickNumAxes(joystick1)
print('axis={}'.format(axes))
balls = joystick.SDL_JoystickNumBalls(joystick1)
print('balls={}'.format(balls))
hats = joystick.SDL_JoystickNumHats(joystick1)
print('hats={}'.format(hats))
buttons = joystick.SDL_JoystickNumButtons(joystick1)
print('buttons={}'.format(buttons))
window = sdl2.ext.Window('Test', size=(640, 480))
window.show()

key_states = sdl2.SDL_GetKeyboardState(None)
# hats = joystick.SDL_JoystickNumHats(joystick1)
# print(hats)
# for state in (SDL_IGNORE, SDL_ENABLE):
#     news = joystick.SDL_JoystickEventState(state)
#     print(news, state)
# for axis in range(joystick.SDL_JoystickNumAxes(joystick1)):
#     val = joystick.SDL_JoystickGetAxis(joystick1, axis)
#     print(val, axis)
# for button in range(joystick.SDL_JoystickNumButtons(joystick1)):
#     val = joystick.SDL_JoystickGetButton(joystick1, button)
#     print(val, button)
# while 1:
    # for event in sdl2.ext.get_events():
        # if event.type == sdl2.SDL_KEYDOWN:
            # print(event.key.keysym.sym)
#         elif event.type == sdl2.SDL_JOYBUTTONUP:
#             print(event.jbutton.button)
#         elif event.type == sdl2.SDL_JOYAXISMOTION:
#             print([event.jaxis.axis, event.jaxis.value])
#         elif event.type == sdl2.SDL_JOYHATMOTION:
#             print([event.jhat.hat, event.jhat.value])
    # event = sdl2.SDL_JoystickCurrentPowerLevel(joystick1)
    # print(event)
    # time.sleep(0.01)
key_down = False
while 1:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False
            break
    if key_states[sdl2.SDL_SCANCODE_A] and not key_down:
        print('A key pressed')
        key_down = True
    elif not key_states[sdl2.SDL_SCANCODE_A] and key_down:
        print('A key released')
        key_down = False
    window.refresh()
