from PyQt5.QtCore import QObject, pyqtSignal, QThread
from Temp.math.button_dict import axis
import sdl2.ext
import time


class Joystick(QObject):

    sign_button = pyqtSignal()  #
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
            time.sleep(1)
            sdl2.SDL_JoystickOpen(0)
            while num:
                for event in sdl2.ext.get_events():
                    if event.type == sdl2.SDL_JOYAXISMOTION:
                        print(1)


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    #
    __joystick = Joystick()
    #
    sys.exit(app.exec_())
