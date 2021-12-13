class _ArtNet:

    DELAY = 0.5
    PORT = 6454  # ArtNet UDP固定端口
    OPCODE = [0x00, 0x50]  # 传输方式定义
    VERSION = [0x00, 0x0e]  # ArtNet版本号
    SEQUENCE = 0x00  # 禁止乱序自动排列功能
    PHYSICAL = 0x00  # 物理端口，默认为0

    PKT_LEN = 512  # 数据长度最大512
    IMG_PIXEL = 600  # 实际单通道控制Led数
    PHY_PIXEL = 680  # 单通道最大可控制Led数
    UNIVERSE_PIXEL = 170  # 单指令可控制Led数

    CHANNELS = dict()
    for i in range(16):
        CHANNELS[i] = [i for i in range(4 * i, 4 * (i + 1))]


class _LedWall:

    DELAY = 1 / 8
    COLS = 80  # 列
    ROWS = 120  # 行

    LENGTH = 7.083  # 长
    HIGH = 2  # 高


class _Show:

    # IMG
    THANKS = 0
    WELCOME = 1
    # VIDEO
    SKY = 0
    SEA = 1
    # COLOR
    R = 0
    G = 1
    B = 2
    BLINK = 3
    COLORFUL = 4

    IMG = {THANKS: 'thanks.jpeg',
           WELCOME: 'welcome.png'}
    VIDEO = {SKY: 'sky.mp4',
             SEA: 'sea.mp4'}
    COLOR = {R: 100,
             G: 100,
             B: 100}


class _Anet:

    PORT = {1: 24199,
            2: 24200}
    SHOW_HEAD = b'\xfe\xff'
    COLOR_HEAD = b'\xfe\xfe'


class _Test:

    MACHINE_SN = 'LED_WALL3'


class _Const:

    ARTNET = _ArtNet()
    LED = _LedWall()
    SHOW = _Show()
    ANET = _Anet()
    TEST = _Test()


CONST = _Const()
