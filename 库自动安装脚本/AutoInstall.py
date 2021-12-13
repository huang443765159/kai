import multiprocessing
import os

'注意事项：需要现在git上配置ssh密钥'

LIBS = ['XYZCFD3', 'XYZConfig3', 'XYZDoors3', 'XYZGuides3', 'XYZHologram3', 'XYZJoystick3',
        'XYZLeds3',  'XYZLidars3', 'XYZLog3', 'XYZMothers3', 'XYZMotors3', 'XYZMotors3Plugin',
        'XYZNetwork3', 'XYZPaths3', 'XYZScenes3', 'XYZSwitches3', 'XYZTV3', 'XYZVisual3',
        'XYZWorkFlow3']


class _CONST:
    TAR_FILE = os.path.expanduser('~/Documents/CODES')
    if not os.path.exists(TAR_FILE):
        os.makedirs(TAR_FILE)
    GIT_PATH = 'git@github.com:WillEEEEEE'


class AutoInstall:

    @staticmethod
    def _check_lib(lib: str):
        if not os.path.exists(os.path.join(_CONST.TAR_FILE, lib)):
            os.system(f"cd {_CONST.TAR_FILE}; git clone {os.path.join(_CONST.GIT_PATH, lib + '.git')}")
        else:
            os.system(f"cd {os.path.join(_CONST.TAR_FILE, lib)}; git pull")
        os.system(f'cd {os.path.join(_CONST.TAR_FILE, lib)}; pip3 install .')

    def run(self):
        pool = multiprocessing.Pool(processes=5)
        for lib in LIBS:
            pool.apply_async(func=self._check_lib, args=(lib, ))
        pool.close()
        pool.join()


if __name__ == '__main__':
    test = AutoInstall()
    test.run()
