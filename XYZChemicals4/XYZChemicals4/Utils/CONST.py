from .Singleton import singleton


class _Tank:
    WIDTH = 10
    HEIGHT = 10
    LENGTH = 10


class _Devices:
    M3 = 10
    ACID = 11
    WHEELS = 12
    WAX = 13
    PUMP = 14


@singleton
class _Const:
    TANK = _Tank()
    DEVICES = _Devices()


CONST = _Const()
