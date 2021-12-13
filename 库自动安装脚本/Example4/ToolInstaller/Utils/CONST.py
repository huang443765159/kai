import os


LIBS = ['XYZCFD3', 'XYZConfig3', 'XYZDoors3', 'XYZGuides3', 'XYZHologram3', 'XYZJoyStick3',
        'XYZLeds3', 'XYZLidars3', 'XYZLog3', 'XYZMothers3', 'XYZMotors3', 'XYZMotors3Plugin',
        'XYZNetwork3', 'XYZPaths3', 'XYZScenes3', 'XYZSwitches3', 'XYZTV3', 'XYZVisual3',
        'XYZWorkFlow3']

MONTH_MAP = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6',
             'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

# a = [, 'XYZConfig3', 'XYZDoors3', 'XYZGuides3', 'XYZHologram3', 'XYZJoyStick3',
#         'XYZLeds3', 'XYZLidars3', 'XYZLog3', 'XYZMothers3', 'XYZMotors3', 'XYZMotors3Plugin',
#         'XYZNetwork3', 'XYZPaths3', 'XYZScenes3', 'XYZSwitches3', 'XYZTV3', 'XYZVisual3',
#         'XYZWorkFlow3']

class _Const:
    TAR_FILE = os.path.expanduser('~/Documents/CODES')
    if not os.path.exists(TAR_FILE):
        os.makedirs(TAR_FILE)
    GIT_PATH = 'git@github.com:WillEEEEEE'


CONST = _Const()

