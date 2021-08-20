from PyQt5.QtCore import QObject, pyqtSignal, QThread
import sdl2.ext
import time


class Joystick(QObject):

    sign_button = pyqtSignal(str)  #
    sign_axis = pyqtSignal()  #
    sign_connect = pyqtSignal()  #

    def __init__(self):
        super().__init__()
        # self._working()
        # THREAD
        self._thread = QThread()
        self.moveToThread(self._thread)
        self._thread.started.connect(self._working)
        self._thread.start()

    def _working(self):
        sdl2.SDL_Quit(sdl2.SDL_INIT_JOYSTICK)
        sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
        sdl2.joystick.SDL_NumJoysticks()
        sdl2.SDL_JoystickOpen(0)
        while 1:
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_JOYBUTTONDOWN:
                    self.sign_button.emit('{}'.format(event.jbutton.button))
            time.sleep(0.01)


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    #
    __joystick = Joystick()
    __joystick.sign_button.connect(print)
    #
    sys.exit(app.exec_())