import os


LIBS = ['XYZCFD3', 'XYZConfig3', 'XYZDoors3', 'XYZGuides3', 'XYZHologram3', 'XYZJoyStick3',
        'XYZLeds3', 'XYZLidars3', 'XYZLog3', 'XYZMothers3', 'XYZMotors3', 'XYZMotors3Plugin',
        'XYZNetwork3', 'XYZPaths3', 'XYZScenes3', 'XYZSwitches3', 'XYZTV3', 'XYZVisual3',
        'XYZWorkFlow3']


class _Const:
    TAR_FILE = os.path.expanduser('~/Documents/CODES')
    if not os.path.exists(TAR_FILE):
        os.makedirs(TAR_FILE)
    GIT_PATH = 'git@github.com:WillEEEEEE'


CONST = _Const()

