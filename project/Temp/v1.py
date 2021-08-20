from PyQt5.QtCore import QObject, pyqtSignal, QThread
from Temp.math.button_dict import buttons, axis, get_value
import sdl2.ext
import time


class Joystick(QObject):

#     sign_button = pyqtSignal(str, bool)  # button, state
    sign_axis = pyqtSignal()
#     sign_connect = pyqtSignal()

    def __init__(self):
        super().__init__()
#         # THREAD
        self._thread = QThread()
        self.moveToThread(self._thread)
        self._thread.started.connect(self._working)
        self._thread.start()

    def _working(self):
        sdl2.SDL_Quit(sdl2.SDL_INIT_JOYSTICK)
        sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
        #  初始化
        a = sdl2.joystick.SDL_NumJoysticks()
        sdl2.SDL_JoystickOpen(0)
        if a:
            while 1:
                try:
                    for event in sdl2.ext.get_events():
                        if event.type == sdl2.SDL_JOYAXISMOTION:
                            # print([event.jaxis.axis, event.jaxis.value])
                            value = get_value(event.jaxis.value)
                            joy_axis = [event.jaxis.axis, value]
                            for key, value in axis.items():
                                if joy_axis == value:
                                    self.sign_axis.emit(key)
                            if event.jaxis.axis == 4 or event.jaxis.axis == 5:
                                if event.jaxis.value == -32768:
                                    print(axis[event.jaxis.axis], False)
                                else:
                                    print(axis[event.jaxis.axis], True)
                    time.sleep(0.01)
                except:
                    break
        else:
            time.sleep(0.5)

if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    #
    __joystick = Joystick()
    __joystick.sign_axis.connect(print)
    #
    sys.exit(app.exec_())