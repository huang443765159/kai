from PyQt5.QtCore import QObject, pyqtSignal, QThread, pyqtSlot
from Temp.math.button_dict import buttons, axis
import sdl2.ext
import time


class Joystick(QObject):

    sign_button = pyqtSignal(str, bool)  # button, state
    sign_axis = pyqtSignal()  #
    sign_connect = pyqtSignal()  #

    def __init__(self):
        super().__init__()
        # THREAD
        self._thread = QThread()
        self.moveToThread(self._thread)
        self._thread.started.connect(self._working)
        self._thread.start()


    def _working(self):
        while 1:
            sdl2.SDL_Quit(sdl2.SDL_INIT_JOYSTICK)
            sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
            #  初始化
            num = sdl2.joystick.SDL_NumJoysticks()
            if num:
                while 1:
                    try:
                        sdl2.SDL_JoystickOpen(0)
                        for event in sdl2.ext.get_events():
                            if event.type == sdl2.SDL_JOYBUTTONDOWN:
                                if event.jbutton.button in buttons.keys():
                                    self.sign_button.emit(buttons[event.jbutton.button], True)
                            elif event.type == sdl2.SDL_JOYBUTTONUP:
                                if event.jbutton.button in buttons.keys():
                                    self.sign_button.emit(buttons[event.jbutton.button], False)
                            # elif event.type == sdl2.SDL_JOYAXISMOTION:
                            #     pass

                        time.sleep(0.01)
                    except IOError:
                        print(1)
                        break
            else:
                print('Searching ...')
                time.sleep(0.5)


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    #
    __joystick = Joystick()
    __joystick.sign_button.connect(print)
    #
    sys.exit(app.exec_())
