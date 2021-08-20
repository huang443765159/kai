import sdl2.ext


class Test(object):

    def __init__(self):
        super().__init__()

    def callback(self, sender):
        self.sender = sender
        if sender.type == sdl2.SDL_JOYBUTTONDOWN:
            print(sender.jbutton.button)


if __name__ == '__main__':

    _test = Test()
