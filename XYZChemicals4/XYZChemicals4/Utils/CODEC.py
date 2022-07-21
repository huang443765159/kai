from .Singleton import singleton


@singleton
class _Code:
    READ = b'\xea'  # 回复所有泵的状态
    WRITE = b'\xeb'
    ERROR = b'\xee'
    LEVEL = b'\xed'
    SENSORS = b'\x71'  # 温湿度传感器
    PRESSURE = b'\xef'  # 压力
    FLOW = b'\xec'  # 流量


CODEC = _Code()
