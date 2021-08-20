class _ArtNet:

    DELAY = 0.3
    PORT = 6454  # ArtNet 固定端口
    OPCODE = [0x00, 0x50]  # 传输方式定义
    VERSION = [0x00, 0x0e]  # ArtNet版本号
    SEQUENCE = 0x00  # 禁止乱序自动排列功能
    PHYSICAL = 0x00  # 物理端口，默认为0

    UNIVERSES = dict()
    for i in range(16):
        UNIVERSES[i] = [i for i in range(4 * i, 4 * i + 4)]
    print(UNIVERSES)


class _Const:

    ART_NET = _ArtNet()


CONST = _Const()
