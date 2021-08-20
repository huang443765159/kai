import sdl2.ext
import time


def main():
    while 1:
        sdl2.SDL_Quit(sdl2.SDL_INIT_JOYSTICK)
        sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
        num = sdl2.joystick.SDL_NumJoysticks()
        joy = sdl2.SDL_JoystickOpen(0)
        sdl2.SDL_JoystickUpdate(joy)
        print('Joystick_sum =', num, joy)
        time.sleep(1)


if __name__ == '__main__':

    main()

